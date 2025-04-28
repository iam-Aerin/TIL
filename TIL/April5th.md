
*4월 5주차*

```[main folder name will be added soon.......]```
> `tableu.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._


---

# Tableau
# 데이터 시각화
> 
> https://help.tableau.com/current/guides/get-started-tutorial/en-us/get-started-tutorial-home.htm?_gl=1*1d87mx9*_ga*MTQwMzk0NzAxOC4xNzQ0MjY1NzI0*_ga_8YLN0SNXVS*MTc0NTgwMDkyNy41LjEuMTc0NTgwMDk5OC4wLjAuMA..

- Public Tableau 버전 설치
> https://public.tableau.com/app/discover 

-  Tableau 샘플 데이터
> https://public.tableau.com/app/learn/sample-data?_gl=1*lta7eb*_ga*ODI4ODUxMjQwLjE3NDU4MDE1NDc.*_ga_8YLN0SNXVS*MTc0NTgwMTU0Ni4xLjAuMTc0NTgwMTU0Ni4wLjAuMA..
>
> `슈퍼스토어 매출	이 가상 회사에서 주요 개선 영역을 식별하는 데 도움이 되는 제품, 매출, 수익 등에 대한 정보가 들어 있습니다.` 슈퍼 스토어 데이터 사용

![tableu worksheet](/assets/tableau_worksheet.png)

---
## Tableau 관련 용어어
# Create a View

You set out to identify key areas for improvement, but where to start?  
With four years' worth of data, you decide to drill into the overall sales data to see what you find.  
Start by creating a simple chart.

> **Learn more: Terms in this section**

| **Term**                | **Description** |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Aggregation**: 집계         | Row-level data rolled up to a higher category, such as sum of sales or total profit. Tableau does this automatically so you can break data down to the level of detail that you want to work with. |
| **Dimension vs Measure**: 차원 및 측정값 | Dimensions are qualitative data, such as a name or date. By default, Tableau automatically classifies data that contains qualitative or categorical information as a dimension, for example, any field with text or date values. These fields generally appear as column headers for rows of data, such as Customer Name or Order Date, and also define the level of granularity that shows in the view.<br><br>Measures are quantitative numerical data. By default, Tableau treats any field containing this kind of data as a measure, for example, sales transactions or profit. Data that is classified as a measure can be aggregated based on a given dimension, for example, total sales (Measure) by region (Dimension). |
| **Continuous vs Discrete**: 연속형 및 불연속형 | Continuous fields can contain an infinite number of values. This can be a range of values such as sales within a specific date range or quantities. Continuous fields are coloured green in Tableau.<br><br>Discrete fields contain a finite number of values such as country, state, or customer name. Discrete fields are coloured blue in Tableau. |

---
- 측정값은 `차원`/ e.g. `날짜`는 '연속적인 측정값'/ `글자`는 '불연속적인 측정값'

# Tableau: Key Concepts 정리

## 1. Aggregation

- **정의**:  
  Row-level data를 요약하여 더 높은 수준(합계, 평균 등)으로 집계하는 것.
  Tableau는 기본적으로 데이터를 자동 집계하여 표시합니다.

- **표현 색상**:  
  - 별도로 색상 표현은 없음. (Aggregation은 차트 계산 로직에 해당)

- **예시**:  
  - 전체 매출 총합 (`SUM(Sales)`)
  - 평균 주문 금액 (`AVG(Order Amount)`)
  - 최대 이익 (`MAX(Profit)`)

---

## 2. Dimension vs Measure

| 구분 | 설명 | 색상 | 예시 |
|:---|:---|:---|:---|
| **Dimension** | 범주형 데이터. 데이터를 구분하는 데 사용. | 파란색 (Blue) | - 고객 이름 (Customer Name) <br> - 주문 날짜 (Order Date) <br> - 제품 카테고리 (Product Category) |
| **Measure** | 수치형 데이터. 계산 및 집계 대상이 됨. | 녹색 (Green) | - 매출 (Sales) <br> - 수량 (Quantity) <br> - 이익 (Profit) |

---

## 3. Continuous vs Discrete

| 구분 | 설명 | 색상 | 예시 |
|:---|:---|:---|:---|
| **Continuous** | 값의 범위가 연속적인 필드. 축(Axis) 생성. | 녹색 (Green) | - 연속된 판매 금액 (Sales Amount) <br> - 연도별 매출 (Year over Year Sales) <br> - 수량 (Quantity) |
| **Discrete** | 유한한 수의 고정된 값. 범주(Category) 생성. | 파란색 (Blue) | - 국가 (Country) <br> - 제품 이름 (Product Name) <br> - 고객 ID (Customer ID) |

---

# 요약

- **Dimension** = 파란색 (Blue) → 카테고리 구분용
- **Measure** = 녹색 (Green) → 수치 계산용
- **Continuous** = 녹색 (Green) → 연속된 값 (Axis 생성)
- **Discrete** = 파란색 (Blue) → 고정된 값 (Category 생성)




![tableau_sales_Orderdate_Sales](/assets/tableau_sales_Orderdate_Sales.png)
![tableau_sum](/assets/tableau_sum.png)
> tableau 측정값 변경시 합계/ 평균 등등 계산이 자동으로 적용됨.

![filtering_orderdate](/assets/filtering_orderdate.png)
> 원하는 년도를 필터링해서 볼 수 있음