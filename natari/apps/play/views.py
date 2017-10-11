from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *
import random

options = [
"NUCLEAR BOMB",
"ROACH",
"FOOT",
]
def flip_coin():
    return random.randint(0,1)

def add_pts(request):
    userstats = GameStats.objects.get(user=request.user.id)
    userstats.points += 105
    userstats.save()

def nuclearize(request):
    userstats = GameStats.objects.get(user=request.user.id)
    userstats.nuclear = True
    userstats.save()

def sickness(request):
    userstats = GameStats.objects.get(user=request.user.id)
    userstats.health-= 1
    userstats.save()
    if userstats.health == 0:
        endgame(request)

def endgame(request):
    print("we're ending the game")
    player = User.objects.get(id=request.user.id).profile
    highscore = player.high_score
    print("old high score:", highscore)
    currscore = GameStats.objects.get(user=request.user).points
    player.games_played+=1
    if highscore < currscore:
        player.high_score=currscore
        print("new high score: ", player.high_score)
        player.save()
    curr = GameStats.objects.get(user=request.user)
    curr.health = 5
    curr.points = 0
    curr.twinkies = 0
    curr.nuclear = False
    curr.save()
    return redirect(reverse('dash'))


# Create your views here.
def base(request):
    player = GameStats.objects.get(user=request.user)
    opponent = 'Mr.Roboto'
    context = {
        'player': player,
        'opponent': opponent,
    }
    if request.method == "POST":
        move(request, player)
        return redirect(reverse('play:base'))
    return render(request, 'play/game.html', context)

def move(request, player):
    # if user2 == None:
        # if playing against computer, user2 will not be passed so generate a play
    user2 = options[random.randint(0,2)]
    user1 = request.POST['move']
    print(user1,user2)
    if user1 == options[1]:
        # if the user selected roach
        winner = roach_fight(request,player,user1,user2)
    elif user1 == options[2]:
        # if the user selected foot
        winner = foot_fight(request,player,user1,user2)
    elif user1 == options[0]:
        # if the user selected bomb
        if user2 == options[0]:
            # if comp also selects bomb, game ends
            # resets but does not redirect!!!
            return endgame(request)
        else:
            winner = bomb_fight(request,player,user1,user2)
    print(winner)

def roach_fight(request,player,user1,user2):
    # if the user selected roach
    if user2 == options[1]:
        # and the computer also played ROACH, randomise who gets double points
        if flip_coin() == 0:
            winner = "user1"
            add_pts(request)
            add_pts(request)
            print('r-r: win, add pts')
        else:
            winner = "user2"
            print('r-r: lose, no pts')
    elif user2 == options[0]:
        #and the computer plays bomb, randomise if bomb roach survives or bomb lands directly on it
        if flip_coin() == 0:
            #roach lives!!!
            winner = "user1"
            if player.health > 2:
                nuclearize(request)
            add_pts(request)
            print('r-b: win, add pts, maybe nuclear if healthy')
        else:
            #bomb lands on roach
            winner = "user2"
            sickness(request)
            print('r-b: lose, lose health')
    elif user2 == options[2]:
        #and the computer plays foot
        if flip_coin() == 0:
            #foot squishes roach!
            winner = "user2"
            sickness(request)
            print('r-f: lose, lose health')
        else:
            #roach bites the foot
            winner = "user1"
            add_pts(request)
            print('r-f: win, add pts')
    return winner

def foot_fight(request,player,user1,user2):
    # if the user selected foot
    if user2 == options[1]:
        # and the computer played ROACH,
        if flip_coin() == 0:
            #foot squishes roach
            winner = "user1"
            add_pts(request)
            print('f-r: win, add pts')
        else:
            #roach bites the foot
            winner = "user2"
            sickness(request)
            print('f-r: lose, lose health')
    elif user2 == options[0]:
        #and the computer plays bomb, randomise if bomb mutates foot or kills it
        if flip_coin() == 0:
            #foot lives!!!
            winner = "user1"
            if player.health > 2:
                nuclearize(request)
            add_pts(request)
            print('f-b: win, add pts, maybe nuclear if healthy')
        else:
            #foot harmed
            winner = "user2"
            sickness(request)
            print('f-b: lose, lose health')
    elif user2 == options[2]:
        #and the computer plays foot, randomise foot interactions
        if flip_coin() == 0:
            #feet get along
            winner = "user1"
            add_pts(request)
            add_pts(request)
            print('f-f: win, dbl pts')
        else:
            #feet do not get along
            winner = "user2"
            print('f-f: lose, none')
    return winner

def bomb_fight(request,player,user1,user2):
    # if the user selected bomb
    # if user2 == options[0]:
    #     # and the computer also played bomb, game ends
    #     return redirect(reverse('play:endgame'))
    if user2 == options[1]:
        #and the computer plays roach, randomise if roach survives or bomb lands directly on it
        if flip_coin() == 0:
            #roach lives!!!
            winner = "user2"
            sickness(request)
            print('b-r: lose, lose health')
        else:
            #bomb lands on roach
            winner = "user1"
            add_pts(request)
            print('b-r: win, add pts')
    elif user2 == options[2]:
        #and the computer plays foot, randomise if foot mutates
        if flip_coin() == 0:
            #foot mutates
            winner = "user2"
            sickness(request)
            print('b-f: lose, lose health')
        else:
            #bomb kills the foot
            winner = "user1"
            add_pts(request)
            print('b-f: win, add pts')
    return winner
