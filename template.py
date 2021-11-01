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
        outputs={outputs_path: f'-c copy -reset_timestamps 1 -segment_atclocktime 1 -segment_time 3600 -f segment -strftime 1 ',
                 }
    )
    run.run()

try:
    os.mkdir(canal)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

formato = canal+"/"+"1_%Y%m%d_%H%M001"+'.'+formato

try:
    ffmpeg_path(url, formato)
except:
    print("error de cordinacion con la hora, intentando nuevamnete")
    time.sleep(10)
print("fallo se reiniciara la grabacion en el proximo cronb")