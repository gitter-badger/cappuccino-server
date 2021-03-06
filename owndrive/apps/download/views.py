from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import Context, Template
from owndrive import constants
from django.shortcuts import render_to_response
from django.template import loader
from django.http import JsonResponse
from owndrive.local_settings import *
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


class DownloadView(View):

    def get(self, request, *args, **kwargs):
        global currentDir

        print("COMANDO: " + request.GET.get('command', 'ls'))
        currentDir = request.GET.get('currentDir', '/')
        print("Current DIR : " + currentDir)

        command = request.GET.get('command', 'ls')

        file_path = SHARED_PATH + '/' + command.split(" ")[1]
        print("FILE TO DOWNLOAD : " + file_path)

        from django.utils.encoding import smart_str

        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(command.split(" ")[1])
        response['X-Sendfile'] = smart_str(file_path)
        # It's usually a good idea to set the 'Content-Length' header too.
        # You can also set any other required headers: Cache-Control, etc.
        return response
