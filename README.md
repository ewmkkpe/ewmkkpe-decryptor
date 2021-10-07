# ewmkkpe-decryptor

AES CBC 256 bit 로 encryption / decryption 해주는 스크립트입니다.


## Setup

다음과 같은 순서로 세팅할 수 있습니다.

    (project folder) virtualenv -p python3 .venv

    (project folder) source .venv/bin/activate

    (.venv) pip3 install -r requirements.txt

## Key file Setting

    conf/key.json 파일을 생성합니다.

    conf/key.json.sample 파일을 참고해서, AES CBC 256bit encryption에 사용되는 Secret Key 와 128bit IV 값을 기록합니다. (둘 다 HEX encoding 되어 있습니다.)

## Encryption 실행

위의 Key file Setting을 마무리 한 후에 실행해야 합니다.

    (.venv) python3 encryptor.py -i <암호화하고자 하는 String>

### 실행 예시

암호화된 결과도 HEX string으로 나옵니다.
    
    Input String : abcdefghij
    Length of Key : 256 bits Length of IV : 128 bits
    
    [Encrypted Hex string]
    4b74e9b67739d2c2c6635e7f11b66b90
    
    [Human-Readable Encrypted Hex string]
    4b74 e9b6
    7739 d2c2
    c663 5e7f
    11b6 6b90

## Decryption 실행

위의 Key file Setting을 마무리 한 후에 실행해야 합니다.

    (.venv) python3 decryptor.py -e <이미 암호화된 HEX String>

### 실행 예시

평문화된 결과는 다음과 같이 출력됩니다.

    Encrypted Value : 4b74e9b67739d2c2c6635e7f11b66b90
    Length of Key : 256 bits Length of IV : 128 bits
    Encrypted Bytes Length : 16 Bytes
    
    [Decrypted input]
    abcdefghij

## Key Generator 실행

위의 AES encryption/decryption을 위한 암호화 키를 Secret Random을 통해서 생성해냅니다.

    (.venv) python3 key_generator.py

### 실행 예시

    =================================================
    [AES CBC 256 bit Secret Key in Hex]
    8bb8a0f7740e194256f08471b541b61440687dc721c31f9cf98d34daa6289e3d
    
    [Human-Readable HEX string]
    8bb8 a0f7
    740e 1942
    56f0 8471
    b541 b614
    4068 7dc7
    21c3 1f9c
    f98d 34da
    a628 9e3d
    
    =================================================
    [AES CBC 128 bit IV in Hex]
    8dc79a7fa09e9b1420332a0e118ebb8c
    
    [Human-Readable HEX string]
    8dc7 9a7f
    a09e 9b14
    2033 2a0e
    118e bb8c
    
    =================================================
