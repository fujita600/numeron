import random

class NumerOn:
    __original: str     # 比較対象元の数字列

    # original => 比較対象元の数字列
    def __init__(self, original: str | None = None)->bool:
        if original != None:
            return self.setOriginalValue(original)

        self.__original = original = ""
        return True

    # 比較対象元の値をセットするためのモジュール
    def setOriginalValue(self, original: str)->bool:
        self.__original = original
        return self.__original.isdigit() and NumerOn.isStrUnique(self.__original)

    # 引数に指定された値と比較対象元の値を比較して EAT BITE を求める
    # 
    # tuple => 処理成功
    # None  => 処理失敗
    def check(self, value: str)->tuple | None:
        eat = 0
        bite = 0
        val_len = 0

        # 文字列の長さが等しくないときにはエラーを返す
        if len(value) != len(self.__original):
            return None

        if not value.isdigit():
            return None

        if NumerOn.isStrUnique(value) == False:
            return None

        val_len = len(value)
        for i in range(0, val_len, 1):
            if self.__original[i] == value[i]:
                eat += 1
            elif self.__original.find(value[i]):
                bite += 1

        return (eat, bite)

    # 比較対象元の値を動的に生成するためのモジュール
    #
    # makeOrigianlValue(5)
    #  => "53124"
    @staticmethod
    def makeOrigianlValue(nbr: int = 3)->str:
        ret = ""
        asc_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # asc_numberの情報をシャッフルする
        for i in range(0, len(asc_number), 1):
            rand = random.randint(0, nbr)

            stk = asc_number[rand]
            asc_number[rand] = asc_number[i]
            asc_number[i] = stk

        # 先頭から文字列に対して値を末尾に追加していく
        for i in range(0, nbr, 1):
            ret += str(asc_number[i])
        
        return ret

    # 文字列がユニークかどうかのチェックモジュール
    @staticmethod
    def isStrUnique(s: str)->bool:
        s_len = len(s)

        for i in range(0, s_len, 1):
            for j in range(i + 1, s_len, 1):
                if s[i] == s[j]:
                    return False
        return True

    # 答えの可能性を配列で返すモジュール
    @staticmethod
    def forecast(request: list, hit: int, blow: int):
        """
        @params request -> 予測値
        @params hit -> 予測値のヒットの数
        @params blow -> 予測値のブローの数
        """
        result = []     # 戻り値
        

