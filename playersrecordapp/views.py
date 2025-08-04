 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializers import PlayerSerializer


@api_view(['POST'])
def insert_player(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_one_player(request, jn):
    try:
        player = Player.objects.get(jn=jn)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PlayerSerializer(player)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_batsmen(request):
    batsmen = Player.objects.filter(runs__gt=0)
    serializer = PlayerSerializer(batsmen, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_bowlers(request):
    bowlers = Player.objects.filter(wickets__gt=0)
    serializer = PlayerSerializer(bowlers, many=True)
    return Response(serializer.data)
