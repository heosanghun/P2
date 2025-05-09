# paper2 패키지 초기화 

import os
import sys

# Paper1 디렉토리 경로 추가
paper2_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(paper2_dir)
paper1_dir = os.path.join(root_dir, 'paper1')

# Python 경로에 Paper1 디렉토리 추가
if paper1_dir not in sys.path:
    sys.path.insert(0, paper1_dir)

# Paper2 모듈 버전 정보
__version__ = '1.0.0' 