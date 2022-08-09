import os
import traceback

from airtest_ocr.arena.api import Arena


base_pth = os.path.dirname(__file__).replace('\\', '/')
model_pth = '/'.join(base_pth.split('/')[:-1]) + '/models/'

try:
    OCR_ENGINE = Arena(model_dir=model_pth)
    OCR_ENGINE.load_lite_models()
except FileNotFoundError:
    from airtest_ocr.utils.download import download
    download("lite-onnx", model_pth, base_pth)
    OCR_ENGINE = Arena(model_dir=model_pth)
    OCR_ENGINE.load_lite_models()
except Exception as e:
    traceback.print_exc()
    print(f"Fail to load OCR function.")
    raise Exception


def switch_to_lite():
    try:
        OCR_ENGINE.load_lite_models()
    except FileNotFoundError:
        from airtest_ocr.utils.download import download
        download("lite-onnx", model_pth, base_pth)
        OCR_ENGINE.load_lite_models()
    except Exception:
        raise Exception


def switch_to_full():
    try:
        OCR_ENGINE.load_full_models()
    except FileNotFoundError:
        from airtest_ocr.utils.download import download
        download("full-onnx", model_pth, base_pth)
        OCR_ENGINE.load_full_models()
    except Exception:
        raise Exception


def download_other_models():
    from airtest_ocr.utils.download import download
    download("keyboard-onnx", model_pth, base_pth)
