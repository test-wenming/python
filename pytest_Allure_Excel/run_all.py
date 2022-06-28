
# 要生成pytest-html报告，执行这个
import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-v', '--capture=sys', '--html=./cases/html-report/report.html', '--self-contained-html'])
