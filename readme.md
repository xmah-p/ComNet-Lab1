我在 `./corpus/testmedia` 下放了几个样例视频和一个格式转换脚本 (`converter.py`). 

助教的 `loss.py` 和 `throughput.py` 在 `./corpus` 下. 

```bash
# 传输视频
sudo docker run -d --rm -v `pwd`/corpus:/app -w /app --name alphartc alphartc peerconnection_serverless receiver_pyinfer.json
sudo docker exec alphartc peerconnection_serverless sender_pyinfer.json

# 将 mp4 视频文件转换为 yuv 格式
ffmpeg -i sample0_1280x720.mp4 -c:v rawvideo -pixel_format yuv420p sample0_1280x720.yuv

# 播放 yuv 视频文件
ffplay -f rawvideo -pixel_format yuv420p -video_size 1280x720 -i sample0_1280x720.yuv
```

