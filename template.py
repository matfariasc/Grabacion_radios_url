from ffmpy3 import FFmpeg
import datetime
import time
import os
import sys
import errno

#version para integra-metrics

# variables entorno
canal = sys.argv[1] #nombre de canal
url = sys.argv[2] #URL
formato = sys.argv[3] #MP3 o AAC depende del streming , no hacemos reconversion de todo a un solo formato ya que esto es solo un respaldo en caso de emergencias
# funcion


def ffmpeg_path(inputs_path, outputs_path):
    run = FFmpeg(
        inputs={inputs_path: None},
        outputs={outputs_path: f'-c copy -reset_timestamps 1 -t 00:30:00 -f segment -segment_time 3800 -strftime 1 ',
                 }
    )
    run.run()

parent_dir = "/var/www/html"
path = os.path.join(parent_dir,canal)


try:
    os.mkdir(path)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

formato_mp3 = "mp3"
formato_acc = "aac"
formato = "/var/www/html/"+canal+"/"+"1_%Y%m%d_%H%M001"+'.'+formato_mp3

try:
    ffmpeg_path(url, formato)
    print("FORMATO MP3")
    time.sleep(1)
except:
    ffmpeg_path(url, formato)
    formato = "/var/www/html/"+canal+"/"+"1_%Y%m%d_%H%M%S"+'.'+formato_aac
    print("FORMATO AAC")
    time.sleep(1)
print("fallo se reiniciara la grabacion en el proximo cronb")