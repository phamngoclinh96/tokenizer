import string
import en_core_web_sm

cdau = u"àảãáạăằẳẵắặâầẩẫấậèẻẽéẹêềểễếệìỉĩíịòỏõóọôồổỗốộơờởỡớợùủũúụưừửữứựỳỷỹýỵđÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬÈẺẼÉẸÊỀỂỄẾỆÌỈĨÍỊÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢÙỦŨÚỤƯỪỬỮỨỰỲỶỸÝỴĐ"
alphabet = string.ascii_letters + string.digits + cdau + " ~!@#$%^&*()_+-=[]\;',./{}|:\"<>?"
nlp = en_core_web_sm.load()
def remove(text):
    return ''.join(c for c in text if c in alphabet)

def tokenizer(text):
    return list(nlp(text))

def match(text):
    return text

