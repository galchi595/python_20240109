p=input("일본 여행 계획표를 입력하세요: ")
print(f"일본 여행 계획입니다: {p.split(',')}")

f="""The rock music was booming, the dancers on stage were gyrating, and the crowd was going wild waving thousands of Taiwan flags.
The political rally held on Saturday for the Kuomintang's (KMT) candidate for the 13 January presidential election was in full swing.
"Give me a president!" shouted the host. "Hou You-ih!" the crowd roared.
As Mr Hou looked on, his running mate Jaw Shaw-kong took the microphone and launched a broadside against the ruling Democratic Progressive Party (DPP).
"What road are they taking? The road to war!" he said, wagging his finger. "The road that leads Taiwan into danger, the road that leads to uncertainty!"
As Taiwan edges closer to the election this weekend, the KMT is banking on convincing voters they face a choice between war and peace with China.
Beijing claims the self-ruled island as its own, and while it promotes "peaceful reunification" it has also not ruled out the use of force in taking Taiwan.
In the last eight years of pro-sovereignty DPP rule, China has relentlessly ramped up its military presence around Taiwan, conducting what is known as greyzone warfare.
What's behind China-Taiwan tensions?
China and Taiwan: A really simple guide
How popcorn chicken and bento showcase Taiwan's thorny politics
The DPP has countered that they also want peace and stability - while maintaining Taiwan's path of progress.
A recent viral campaign advertisement showed outgoing President Tsai Ing-wen calmly driving on quiet country roads with her party's presidential candidate William Lai. She then gets out and Mr Lai takes the wheel with his running mate Hsiao Bi-Khim by his side. "Drive better than me," Ms Tsai urges them.
But some are sceptical he can do the job.
At the KMT rally in Taoyuan, an area known for its hardcore supporters, many of those interviewed by the BBC were more concerned with the economy and cost of living. But relations with China also loomed large.
"I didn't use to think there could be war, but now we have this possibility and it's scary. The DPP is just too aggressive, I want to go back to peace with the KMT," said Ms Shi, a 45-year-old service worker accompanying her parents.
"We need to learn from China and how they take care of their citizens. Look at their high-speed railways, their infrastructure. China is so advanced, even their phones are better. We don't have that," said a 58-year-old woman named Ms Tu."""
a=str(input("어떤 단어의 개수가 궁금하나요?: "))
print(f"{a}의 개수는 {f.count(a)}개 입니다")

co=[4000,5000,5500]
ca=[5000,6000,5500]
cco=int(input("1,2,3번중 주문하실 매뉴"))-1
cca=int(input("1,2,3번중 주문하실 매뉴"))-1
print(f"가격은 {co[cco]+ca[cca]}입니다")

b=input("좋아하는 3개의 커피 브랜드를 입력하세요: ").split(',')
for i in range(3):
    b[i]=b[i].capitalize()
print(b)


