-- 코드를 입력하세요
# SELECT A.USER_ID, A.PRODUCT_ID
# FROM ONLINE_SALE AS A JOIN ONLINE_SALE AS B
# ON A.USER_ID = B.USER_ID AND A.PRODUCT_ID = B.PRODUCT_ID
# WHERE A.ONLINE_SALE_ID != B.ONLINE_SALE_ID
# ORDER BY USER_ID ASC, PRODUCT_ID DESC
SELECT DISTINCT A.USER_ID, A.PRODUCT_ID
FROM ONLINE_SALE AS A JOIN ONLINE_SALE AS B
ON A.USER_ID = B.USER_ID AND A.PRODUCT_ID = B.PRODUCT_ID
WHERE A.ONLINE_SALE_ID != B.ONLINE_SALE_ID
ORDER BY A.USER_ID, A.PRODUCT_ID DESC
