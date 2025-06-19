# kavana

## 개요

- RPA프로그램을 python으로 작성하지 않고 script언어로 작성하기 위해서 출발한 프로젝트이다.
- 기본적으로 RPA 동작을 위해서 작성되었으나 개발과정에서 OCR, scrapping, network등 몇가지 기능도 추가되었다.
- 첫 아이디어는 컴퓨터 언어적인 기능 즉 순차적흐름, 조건분기, 루핑등의 기능에 RPA명령어를 섞어서 동작하도록 하는 것이다.
- RPA관련 라이브러리 작성
- 그것을 이용해서 kfs-rpa-script 생성
- 최종적으로는 kfs-auto.exe, a.kas, .env  제공한다.

## kavana 실행파일 생성
```bash
./make.sh
ls ~/bin
kavana --version
```
- make.sh은 pyinstaller롤 실행파일을 만듭니다.
- onedir옵션으로 만듭니다. (onefile 옵션은 실행시 마다 압축을 풀게 되므로 불리)
- onefile 옵션도 가능함.

```bash
./make.sh           # 기본: --onedir
./make.sh onefile   # 명시적: --onefile
./make.sh onedir    # 빠른 실행을 위한 --onedir 빌드
```

## mkdocs사용

```shell
mkdocs serve           # 브라우저로 확인
mkdocs build           # site/ 폴더 생성
mkdocs gh-deploy       # GitHub Pages로 배포 가능
```


## 단위 테스트 및 품질 검사.

- run_test.sh
- vulture  : vulture /lib
- pylint --generate-rcfile > .pylintrc

