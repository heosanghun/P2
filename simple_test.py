#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Paper2에서 DeepSeek 모델 테스트를 위한 간단한 스크립트
"""

import os
import sys
import logging
from datetime import datetime

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 현재 디렉토리와 상위 디렉토리 경로
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
paper1_dir = os.path.join(parent_dir, 'paper1')

# Paper1 디렉토리를 Python 경로에 추가
if paper1_dir not in sys.path:
    sys.path.insert(0, paper1_dir)
    logging.info(f"Paper1 디렉토리를 Python 경로에 추가: {paper1_dir}")

# DeepSeek 모델 테스트
try:
    # Paper1의 OllamaSentimentAnalyzer 모듈 임포트
    from ollama_sentiment_analyzer import OllamaSentimentAnalyzer
    logging.info("Paper1의 OllamaSentimentAnalyzer 모듈 임포트 성공")
    
    # 결과 디렉토리 생성
    results_dir = os.path.join(current_dir, "results", f"deepseek_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    os.makedirs(results_dir, exist_ok=True)
    logging.info(f"결과 디렉토리 생성: {results_dir}")
    
    # DeepSeek 모델 설정
    config = {
        'model_name': 'deepseek-llm:latest',
        'use_deepseek_r1': True,
        'offline_mode': False,
        'output': {
            'save_dir': results_dir
        }
    }
    
    # OllamaSentimentAnalyzer 초기화
    logging.info("DeepSeek 모델 초기화 중...")
    analyzer = OllamaSentimentAnalyzer(config)
    
    # 테스트용 암호화폐 뉴스
    test_text = "Bitcoin has reached a new all-time high as institutional investors continue to show interest in the cryptocurrency."
    
    # 감성 분석 수행
    logging.info(f"테스트 문장 분석 중: {test_text}")
    result = analyzer.analyze(test_text)
    
    # 결과 출력
    logging.info(f"DeepSeek 감성 분석 결과: {result.get('overall_sentiment', 'unknown')}, 점수: {result.get('sentiment_score', 0.0):.2f}")
    
    # 결과 저장
    result_file = os.path.join(results_dir, "sentiment_test_result.json")
    analyzer.save_data(result, result_file)
    logging.info(f"결과 저장 완료: {result_file}")
    
    logging.info("DeepSeek 모델 테스트 완료: 성공")
    
except ImportError as e:
    logging.error(f"모듈 임포트 오류: {e}")
    logging.error(f"Python 경로: {sys.path}")
    sys.exit(1)
except Exception as e:
    logging.error(f"테스트 중 오류 발생: {str(e)}")
    sys.exit(1)
