





curl https://sh.rustup.rs -sSf | sh
sudo apt install build-essential
apt-get install libre2-dev


sudo apt install libgtest-dev



sudo apt update
sudo apt install git g++ make
git clone https://github.com/abseil/abseil-cpp.git
cd abseil-cpp
mkdir build && cd build
cmake -DCMAKE_CXX_STANDARD=14 ..
make -j$(nproc)
sudo make install

pip install apache-airflow
