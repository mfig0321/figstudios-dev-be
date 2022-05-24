import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import action

import chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class ChatterBotApiView(APIView):
    """
    Provide an API endpoint to interact with ChatterBot.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = request.data

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse(
            {
                'name': self.chatterbot.name
            }
        )

class ChatterBotTrain(APIView):

    def get(self, request, **kwargs):
        trainer = ChatterBotCorpusTrainer(chatbot)

        trainer.train(
            "chatterbot.corpus.english"
        )

        return JsonResponse({'status': 'ok'}, status=200)
