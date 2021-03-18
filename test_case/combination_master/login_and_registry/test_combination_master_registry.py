# -*- coding: utf-8 -*-
""" 
@Time    : 2021/3/16 18:11
@Author  : liufubin
@FileName: test_combination_master_registry.py
@description: 组合大师注册测试用例
"""
from public_method.request_method import RequestMethod
import requests


class TestCombinationMasterRegistr(object):
    @staticmethod
    def test_get_phonecode():
        """验证获取手机验证码反机器发送"""
        url = 'https://master-test.simuwang.com/Login/getRegisterPhoneCode?nvc=%257B%2522a%2522%253A%2522CF_APP_1' \
              '%2522%252C%2522c%2522%253A%2522CF_APP_1%253Anvc_register%253A1615887671330%253A0.041899200752100185' \
              '%2522%252C%2522d%2522%253A%2522nvc_register%2522%252C%2522j%2522%253A%257B%2522test%2522%253A1%257D' \
              '%252C%2522h%2522%253A%257B%257D%252C%2522b%2522%253A%2522202!ttVjDtcu25Wtj64F7yKcNomBkPX5Nty0IDEcSv' \
              '%252FMM7LTMBQmTPP9NXPBkcU5vtyakjLBpI0tvWDcwlzN60ttNozxtNYc8%252Bt0y8DtsbYE8NKatt0b' \
              '%252FZaN04KtNWaAxYI2tShtsiIX5S60tW0b' \
              '%252FsdEKaO2sRoX87WaKZdK96xPmWwWfBff5PXwNVREf3X8AP3fNs0EZnurA8WLagja6Ilw7BeKagJLAh3jREWR9gkvjtvatt0C' \
              '%252FZdNtM7ttxOd8%252Bt00BttsgHE8MKytv0b%252F%252BaMtE86cqm%252F6mklKaypMqabE6A5XWMi3efoWqM5HnzwwT' \
              '%252B0KV0pHo0Q6SI87nzpCZ9XmYt5cqIM1pklKVdpcoDjwT3bwhMktyX1xaWvESIyBp4%252BWD' \
              '%252Fkl5WtG1MHw9olaEgKdDAGD5gKQRPx3bKJCNh1zkMd0KrJV%252F8KTDPafvPkE4SmttIKESDVCR5WWD' \
              '%252FkDNK7GE9HXKStdC4KwD2hD4AGjRPq349Ja5avzEAdVKrEQx4KdrgkfDyhXNSXtKTp3deo5VWbSEgkXPj1BVDpcoDfLs357' \
              '%252B53Va0zm6A5c5NvdNqmCENedF4eiPTPFUKdsSl91r8e1a93WO2J1mPVK4FihxvHh4yJECfrcr53DnTgSgWNOVnaN' \
              '%252FVFfzJ4Qc37G0Ugb8DNzwsGxnl0Yz5sqQZf4Dmyq0sF1%252BdalGz2UkSjMtlBwDcJheCvIyJ2404Kl6c3JkU7VUtbh2H8' \
              '%252F4gnAah5dLEvNd1L20nftpwyvOkxIoJ9WnN2oO5ZFCni3TUI67YvE0O3Yn4PMmIF24zl67CygjpWCbIJzH0YBjjk3Pv' \
              '%252BeyfEIqYJ73k0ndf6fbYbbb%252FjRjesbC44O%252BUhdhlIusN6y6BvOM6zOTyCR0sFDwv3ncZdrmG' \
              '%252FT3AvBqMFRJbeKOxHQwaN96v' \
              '%252FLVyXqRJGaVdDJ5g5IamybHYEQO6FO3dyAJjEfNb6wTC3pAQvbXHfHqKBc9yeKsvnOBO9ickj60NE9tksDtNCYljxQ' \
              'T07DReCUmEdD4Muj%252BK4L%252FwS6NrX%252FYmtR5WTPTdpJlhPkRsLp7EXmuzAmtniLZ7TOwTqeyss4UYTxRgCWzW7urgai' \
              'fI%252BPU0IQlZKPwtaoMgV9yhtqswYUPCMopJENJShz6L9ngnbsbf9gz5XNhwW2p3hFGguoKAfQSWXmwN6S%252BUFlU2D8ySOXWV' \
              '93CVWc99QYgt9z1tWlR59nyQuJET%252Bh2WabkgFOYo2YrZ4uxQqrKTcATFomLdMC3GQ22QP2QAW8NngcZvXa%252BbanrGyFSAHr' \
              'JqwvE4OPkwVd9P6MuU6NSgVpU%252BkGyLwlF6ixZnztRhtJ35DJ5UjaMvCU6ut7yUgeiPEUVUHkvCDVGjBeHpxY4zH3ZqWgmznjj78' \
              'EBhqc9p8lS06TvJwF4QtHi35FGvv9K3hHIBSQ%252FsZu1JligdEl7UWfLg8ntVoSjyC%252F5Xof8GGGqqCCJ7k9MakGf93zMFxh5VK' \
              '0lATB5JzdYvKcOazTehNXj%252B%252BC97WzG%252FtHJXCTbR%252Fpup3sMJs%252FAy4Mdi14VjJHaPKjOyCYRS25FXqIwVG0Atud' \
              'HyI%252B4hgFTrtxV4mPZwwKevZOpZmq8SgiUVBvcDXg91Gh7yc7Dhymb9XaW2HWmYGj99ZGw%252BySjZRiTE8vgzjaaJRla6Wtf' \
              'Osr6uM118mtSGQMrAiGxKHGsRmlHEUJlvVQIHEcB2bf7HovZ1stDDIpSvhO3EOgoTKSjYRM%252Fgt1M4uDdF%252FRXxKBIUaBXa' \
              '6eKfQrtcwqn9kHFODTsy9ZNV9nSLBkhcIKbCVmH9CkhuRvaVFa9NJ8HbyX2%252FprxooM7rNLIScY3UZqepOBQ6DTMJz7MEAdXth' \
              'qvVEHEE3GLXeZYLBFnuuFBaBf7rwfe2BM8%252BYn4RpNJiJ19YgnhZ2zXhm%252BEXLQi28x%252FtABV%252FZ8dTwdGlXR%25' \
              '2BdIDj%252BvauQcEbbad3mzIqZ1fwaZAWcqR%252B1SSUMDwWeySzUSrDBh3bsbFGLkP0QVdY2o1m6S4Zmgp29oo0vzpIBclemUe' \
              'rok%252FDDjseEvYDkE3%252BXIQDENCpSYKIsVCnQlPJ7%252FQ67MehBlpePx5k2Nn7PhABrJEuV6UwN%252FmNiKX90Wdn79gf' \
              't1qCP85ED4oTa8DTinP9IOpfEdhmMpkhGafqgNEStYTPNZQeCVxSOsfGA1H2W1R09bQX0m40k%252FltMfjzMuE5htLdsVXmwfM3HK' \
              '1T5lQqN%252BhcBKuIzTP8BfZc6rRpzXoZr9LRb4lzOk%252BW36Spj7IvTHoFPh8VYDLnLHAL6o3eeQ8GlKIDSBCBlZhDi4iEOHhWt' \
              'C%252Fk%252BhAf%252B3wUsJC1Ts8OfYDxGMbsW2QHTu67%252FRTfio6enAPTsyEBlxj84bpMFRs5%252FY1RkQDTFLdbOOhYci' \
              'fUtr1uHf0yRzdybgF%252FlGDkkUczaot2k2XJ4t2%252BjxYVTRAe6Osl5fgRaOxiUed%252B3ho9zw%252FKrWW1YOjaTkg8oRY' \
              'v3vIEJrTXcxT7xVvMAptNabJ9Cv9hql1TqFTthhzDvxHcrG89%252BEWWwS2qce9dfwv8tEv9HRGc%252Br3QdMz1oDgfZ%252FRS' \
              '965dHvTF%252B3vT1HBOgQpgbySXBGIw8CjJ0DY9yQJWKrIDJO39lUQZ%252B6C2pKXzsaHtwj3jg2O6fR9ZRIBmMIMmby6Q7MXyv' \
              'R%252FMArFAp6xJtmxOPnABRgTczPVI7GBDcBmxJZ72tanT0%252FvOT07GCRBVlMICFQOpAUJJb2gwW8KkCwO0wvYrPrjtBvcAq' \
              'Xn7XwTOTk5yQMC8XHwYD%252FBSt0mjGmjk%252BCkmhAyAY7Qc4Brls3TBVD5coqIa1Ic%252B0P1cGVjJXjLyJ%252FAAZ9i%2' \
              '52F9LrbTQwkk0oyOIGOz%252BSQib%252B9B9D1prqsxf8GwZB8%252Fpf7bssKZ7uTofwEgUQRvmsKEN16wBXgzJr7Sd8lzjYjU' \
              'kU4a3yJzWcbF2QLVNlj7CcYp0ptE%252BKULrKOBTnJfElPYtgd4HH5jQsJwJDGeztc2C6UD2kwShHhaOowrWzcka%252BZFPskY' \
              'eYsVWTWEkxDJeMci8boclIu6QxRo4wFsJYtg8tfkh2zImKAuXwzrBbIesygcXGSYWYRBiIm4PKgIQoKA%252BL78jayCxNCka87Y' \
              'Fqfujpl%252BIbomhkqbB%252F7zu5v%252B2CxgD9A4njXFZ7fGOrd7UZxajK6rkAx1Jc9WG5ABz886Kpysyau0lEAKPy2XIKFx' \
              'QaQp2sQxgMNH2%252BQbQVgfbUl8aLUbLC3Zz%252Fz%252FBL0w8GQ47c8iGsSjpw7%252BPcbkBQzT35tLodq6tlby7inMKAgU' \
              '7ka5ydyTrfFAQCNOMpgDLJGmPTovel79g3wdhSuCuoDJCgyB0s%252FW8k5a5YSYR7OcgKpc4TW3Ik2z%252BY6BsV0A2GbrX9tH' \
              'xq0%252BqoCB94VFqOqW1IuaXWCOLebh7JhtPazHU9a9tBpgqLc0EauELETkA0uMIIEwZDyW4co%252Fhm%252Fvtvx%252F3vYZs' \
              'KyvKeDKgUYjvt4gJApcJbu76P0qZWvf%252Bmnq%252BaymsmWcP1EYyP73npsw%252BcUJj6x26277C0y2e3NlcPsX1fbYqAYr%2' \
              '52FmMVqyD4iN49a5VNuLTl6YGCgjwBMcYsrjeb%252Bk%252B9inNT%252F2gARaCP8j5HLECCziHgu3P5eWFPOC%252FqUGLacBw' \
              'bxYyYwjKAH9Tv7ihMB1sOU8pR%252FlKmpvaE7AgzbVUT6SIq7faYiz56L3sgSzLbnjE4xhVniJc2tez0zDDrc2HDhDOTLEOnjiuk' \
              '' \
              'NNL8leTaWR97Rxee6%252BKpOo%252FaIso53jcgTxVI%252BVcwSZFgFCQB2hk%252Bq0MAIVCDcx7Ov74XAdLRqtvvIJym1dNjZ' \
              '%252Fp2hgC9Vi31bdEnIiLhH7pgxxRcBF8ZDHCUPThhjcFlMllLY06BhNgId4gIK2VlGmbrA1Nl3JI8LA61b0VxP%252FfkIYlHYeU' \
              'U4pubpeWAbtwqkwkKS3emdGoNy6YHOmxZDLw%252BPCm04gDQSRrurkGgxeGin%252Bkm7IfBOFN8qyMmtsj4DIxW8G7dOTHK78s' \
              'Cx4zCTNQ7ANJ7P%252F%252FE1fpMylutZpelEvLRul6cFY%252FNPEhRDRO7CCaXt0GRoPHKVvU29ianWJA9QkFO%252BO4rNq' \
              'VhBCko7KkgbbHPgLeGfBKnNZR6xZuvGUOkuKkrEjjK%253D%2522%252C%2522e%2522%253A%2522bDyvu1cJkzsaGol1vOT' \
              'COjPZEkp0u6YUBbX9YU9g2n59tuEUdiugeouLEJG0uvIa-9Z-k-lQ6fL3lpbcTxPN4fk9Wu-Q71ExCDYni5eDYwVSG_W5NXXiw' \
              '0SnMK_GknTTTFhOiVDaaNOdAoCLDoRnw_Ef2lhnqZGFFHdKGjWEu58BL0Bj1jGWPVopmFkTeg5-nggo1h2HkSU45RGVYz2a1Q%2' \
              '522%257D&phone=13055866827&t=1615889618109 '
        result = requests.get(url=url)
        print(result.json())


if __name__ == '__main__':
    TestCombinationMasterRegistr.test_get_phonecode()
