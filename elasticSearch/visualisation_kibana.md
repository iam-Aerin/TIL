# `visualisation_kibana.md`
# Kibana로 시각화하기
> Kibana sample data(e-commerce)데이터로 시각화 연습


- `metric`으로 `Sum of taxful_total_price`를 시각화

![kibana_visualisation_sum](/assets/sum_kibana.png)

![alt text](/assets/bar_categories_order_date.png)

![alt text](/assets/kibana_product_quantity.png)

- 일주일 전 products.quantity 의 sum을 시각화화
![alt text](image-4.png)

- 수식 (이번주 매출액 - 지난주 매출액)
![alt text](/assets/kibana_formula(sum).png)

- 음수는 빨강/ 양수는 파랑으로 색 설정
![alt text](/assets/kibana_colour_range.png)

- map data visualisation
![alt text](/assets/kibana_map.png)

- mau (monthly active users) 시각화
![unique count 시각화](/assets/kibana_uniquecount_mou.png)

- error code (response.keyword 가 500 이상인 서버 이상 에러 코드의 비율) 시각화
![alt text](/assets/kibana_url_error_1.png)

- error code 가 발생하는 url 시각화 
![alt text](/assets/kibana_url_error_2.png)
