
# 克隆 PaddlePaddle 仓库
git clone https://github.com/PaddlePaddle/docs.git

# 定义变量存储仓库路径
repo_path=$(pwd)/docs

# 输出仓库路径
echo "PaddleDoc 仓库路径为: $repo_path"

python gen.py