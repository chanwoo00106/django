# anaconda 사용법

버전 확인
```
conda --version
```

아나콘다 업데이트
```
conda update conda
```

가상환경 생성
```
conda create --name(-n) {가상환경명} {설치할 패키지}
#예
conda create -n test python=3.7
```

가상환경 리스트 확인
```
conda info --envs
```

가상환경 활성화
```
activate {가상환경명}
```

가상환경 비활성화
```
deactivate {가상환경명}
```
