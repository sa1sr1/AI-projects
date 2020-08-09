#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Trigger PiCamera when face is detected."""

from aiy.vision.inference import CameraInference
from aiy.vision.models import face_detection
from picamera import PiCamera
import argparse
import collections
import contextlib
import io
import logging
import math
import os
import queue
import signal
import sys
import threading
import time
from PIL import Image, ImageDraw, ImageFont
from picamera import PiCamera
from aiy.board import Board
from aiy.leds import Color, Leds, Pattern, PrivacyLed
from aiy.toneplayer import TonePlayer
from aiy.vision.streaming.server import StreamingServer
from aiy.vision.streaming import svg
from aiy.vision.inference import ImageInference
from aiy.vision.models import face_detection
import datetime

def take_photo():
            logger.info('Button pressed.')
            player.play(BEEP_SOUND)
            photographer.shoot(camera)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', dest='input', required=True)
    parser.add_argument('--output', '-o', dest='output')
    args = parser.parse_args()
    with ImageInference(face_detection.model()) as inference:
        image = Image.open(args.input)
        draw = ImageDraw.Draw(image)
        faces = face_detection.get_faces(inference.run(image))
        for i, face in enumerate(faces):
            print('%s faces found' % (i))
            x, y, width, height = face.bounding_box
            draw.rectangle((x, y, x + width, y + height), outline='red')
        if args.output:
            image.save(args.output)

    
   

if __name__ == '__main__':
    main()
