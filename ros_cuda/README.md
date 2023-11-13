# Docekr上のcuda環境構築ファイル(動作未確認)
* てきとうに切り貼りして使ってください．
* Dockerfile1行目の`FROM nvidia/cuda:12.2.2-devel-ubuntu20.04`のcudaバージョンは，[docker公式](https://hub.docker.com/r/nvidia/cuda/#!)にあるイメージを参照してください．
* `docker compose build`してから，`docker compose run コンテナ名 Docker上で行いたい処理`で動きます(たぶん)．
