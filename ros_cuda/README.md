# Docekr上のcuda環境構築ファイル(動作未確認)
* てきとうに切り貼りして使ってください．
* Dockerfile1行目の`FROM nvidia/cuda:12.2.2-devel-ubuntu20.04`のcudaバージョンは，
    * nvidia-smiコマンドで出てくるcudaバージョンと，小数点第一位までは合わせてください．
    * [docker公式](https://hub.docker.com/r/nvidia/cuda/#!)にあるイメージを参照してください．
* `docker compose build`してから，`docker compose run cuda-ros python test.py`で``True`が出たらOK．
