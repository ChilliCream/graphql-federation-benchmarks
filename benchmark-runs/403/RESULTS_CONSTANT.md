## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 2,983 | 3,253 | 2,928 | 3.6% |  |
| fusion-nightly-net-10 | 16.7.0-p.28 | 2,756 | 2,905 | 2,747 | 2.0% |  |
| fusion-nightly-net-11 | 16.7.0-p.28 | 2,675 | 2,836 | 2,662 | 2.2% |  |
| fusion-net-10 | 16.6.8 | 2,530 | 2,646 | 2,520 | 1.7% |  |
| hive-router | v0.3.5 | 2,513 | 2,708 | 2,486 | 3.0% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.28 | 2,432 | 2,581 | 2,428 | 2.3% |  |
| grafbase | 0.53.5 | 1,617 | 1,679 | 1,610 | 1.5% |  |
| cosmo | 0.359.0 | 1,424 | 1,484 | 1,416 | 1.6% |  |
| caliban | 3.2.0 | 1,341 | 1,414 | 1,330 | 2.0% |  |
| hive-gateway-router-runtime | 2.15.2 | 514 | 530 | 509 | 1.3% |  |
| apollo-router | v2.18.0 | 452 | 469 | 451 | 1.5% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 396 | 407 | 390 | 1.2% |  |
| apollo-gateway | 2.14.4 | 269 | 274 | 267 | 0.9% |  |
| hive-gateway | 2.15.2 | 267 | 272 | 265 | 1.0% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1074825     ✗ 0     
     data_received..................: 31 GB   261 MB/s
     data_sent......................: 431 MB  3.6 MB/s
     http_req_blocked...............: avg=3.53µs   min=972ns    med=2.68µs  max=18.35ms  p(90)=4.2µs   p(95)=4.92µs   p(99.9)=39.76µs
     http_req_connecting............: avg=275ns    min=0s       med=0s      max=4.27ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=16.52ms  min=976.75µs med=15.97ms max=322.38ms p(90)=24.85ms p(95)=28.27ms  p(99.9)=49.56ms
       { expected_response:true }...: avg=16.52ms  min=976.75µs med=15.97ms max=322.38ms p(90)=24.85ms p(95)=28.27ms  p(99.9)=49.56ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 358375
     http_req_receiving.............: avg=105.01µs min=24.43µs  med=49.74µs max=157.03ms p(90)=96.81µs p(95)=205.49µs p(99.9)=8.65ms 
     http_req_sending...............: avg=55.85µs  min=4.89µs   med=9.91µs  max=170.45ms p(90)=17.24µs p(95)=111.52µs p(99.9)=8.36ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=16.36ms  min=896.6µs  med=15.85ms max=321.98ms p(90)=24.64ms p(95)=27.96ms  p(99.9)=48.51ms
     http_reqs......................: 358375  2983.072144/s
     iteration_duration.............: avg=16.73ms  min=1.46ms   med=16.17ms max=333.09ms p(90)=25.06ms p(95)=28.51ms  p(99.9)=50.19ms
     iterations.....................: 358275  2982.239756/s
     success_rate...................: 100.00% ✓ 358275      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 993822      ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 398 MB  3.3 MB/s
     http_req_blocked...............: avg=3.05µs   min=862ns   med=2.11µs  max=17.99ms  p(90)=3.8µs   p(95)=4.6µs   p(99.9)=33.57µs
     http_req_connecting............: avg=288ns    min=0s      med=0s      max=4.33ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.88ms  min=1.52ms  med=15.88ms max=282.94ms p(90)=28.16ms p(95)=33.65ms p(99.9)=89.68ms
       { expected_response:true }...: avg=17.88ms  min=1.52ms  med=15.88ms max=282.94ms p(90)=28.16ms p(95)=33.65ms p(99.9)=89.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 331374
     http_req_receiving.............: avg=599.58µs min=51.36µs med=85.98µs max=150.15ms p(90)=1.34ms  p(95)=2.55ms  p(99.9)=25.42ms
     http_req_sending...............: avg=49.42µs  min=4.67µs  med=8.59µs  max=148.23ms p(90)=18.43µs p(95)=93.33µs p(99.9)=6.09ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.23ms  min=1.4ms   med=15.31ms max=264.06ms p(90)=27.15ms p(95)=32.52ms p(99.9)=87.45ms
     http_reqs......................: 331374  2756.851412/s
     iteration_duration.............: avg=18.1ms   min=2.2ms   med=16.08ms max=305.47ms p(90)=28.39ms p(95)=33.92ms p(99.9)=90.28ms
     iterations.....................: 331274  2756.019466/s
     success_rate...................: 100.00% ✓ 331274      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 964530      ✗ 0     
     data_received..................: 28 GB   235 MB/s
     data_sent......................: 387 MB  3.2 MB/s
     http_req_blocked...............: avg=2.98µs  min=811ns   med=2.01µs   max=17.82ms  p(90)=3.57µs  p(95)=4.43µs  p(99.9)=28.06µs
     http_req_connecting............: avg=301ns   min=0s      med=0s       max=3.91ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=18.43ms min=1.38ms  med=17.42ms  max=282.96ms p(90)=26.39ms p(95)=30.08ms p(99.9)=51.88ms
       { expected_response:true }...: avg=18.43ms min=1.38ms  med=17.42ms  max=282.96ms p(90)=26.39ms p(95)=30.08ms p(99.9)=51.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 321610
     http_req_receiving.............: avg=1.13ms  min=51.07µs med=115.94µs max=166.54ms p(90)=3.04ms  p(95)=4.32ms  p(99.9)=26.39ms
     http_req_sending...............: avg=47.85µs min=4.44µs  med=8.52µs   max=136.63ms p(90)=18.51µs p(95)=94.69µs p(99.9)=5.58ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.25ms min=1.3ms   med=16.24ms  max=282.74ms p(90)=24.81ms p(95)=28.44ms p(99.9)=48.93ms
     http_reqs......................: 321610  2675.902147/s
     iteration_duration.............: avg=18.65ms min=2.15ms  med=17.62ms  max=296.3ms  p(90)=26.61ms p(95)=30.32ms p(99.9)=52.61ms
     iterations.....................: 321510  2675.070113/s
     success_rate...................: 100.00% ✓ 321510      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 912402      ✗ 0     
     data_received..................: 27 GB   222 MB/s
     data_sent......................: 366 MB  3.0 MB/s
     http_req_blocked...............: avg=4.22µs   min=832ns   med=2µs     max=32.78ms  p(90)=3.52µs  p(95)=4.29µs  p(99.9)=29.57µs 
     http_req_connecting............: avg=1.75µs   min=0s      med=0s      max=32.75ms  p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=19.5ms   min=1.54ms  med=16.44ms max=294.74ms p(90)=31.94ms p(95)=38.99ms p(99.9)=140.97ms
       { expected_response:true }...: avg=19.5ms   min=1.54ms  med=16.44ms max=294.74ms p(90)=31.94ms p(95)=38.99ms p(99.9)=140.97ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 304234
     http_req_receiving.............: avg=549.62µs min=51.43µs med=90.98µs max=173.74ms p(90)=1.05ms  p(95)=1.86ms  p(99.9)=27.2ms  
     http_req_sending...............: avg=44.23µs  min=4.49µs  med=8.34µs  max=162.93ms p(90)=16.51µs p(95)=83.58µs p(99.9)=4.53ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=18.91ms  min=1.45ms  med=15.93ms max=294.61ms p(90)=31.01ms p(95)=37.9ms  p(99.9)=138.76ms
     http_reqs......................: 304234  2530.918714/s
     iteration_duration.............: avg=19.71ms  min=2.07ms  med=16.64ms max=294.97ms p(90)=32.16ms p(95)=39.23ms p(99.9)=141.5ms 
     iterations.....................: 304134  2530.086816/s
     success_rate...................: 100.00% ✓ 304134      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 906138      ✗ 0     
     data_received..................: 26 GB   220 MB/s
     data_sent......................: 363 MB  3.0 MB/s
     http_req_blocked...............: avg=3.03µs  min=881ns   med=2.2µs   max=22.11ms  p(90)=3.77µs  p(95)=4.58µs  p(99.9)=32.11µs
     http_req_connecting............: avg=297ns   min=0s      med=0s      max=3.61ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.63ms min=1.56ms  med=19.36ms max=281.95ms p(90)=27.2ms  p(95)=29.66ms p(99.9)=48.66ms
       { expected_response:true }...: avg=19.63ms min=1.56ms  med=19.36ms max=281.95ms p(90)=27.2ms  p(95)=29.66ms p(99.9)=48.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 302146
     http_req_receiving.............: avg=92.56µs min=27.06µs med=51.83µs max=159.49ms p(90)=94.27µs p(95)=141.9µs p(99.9)=7.26ms 
     http_req_sending...............: avg=44.65µs min=4.8µs   med=9.59µs  max=170.17ms p(90)=17.34µs p(95)=91.81µs p(99.9)=3.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.5ms  min=1.51ms  med=19.24ms max=273.4ms  p(90)=27.05ms p(95)=29.45ms p(99.9)=47.63ms
     http_reqs......................: 302146  2513.617805/s
     iteration_duration.............: avg=19.85ms min=3.55ms  med=19.56ms max=307.97ms p(90)=27.41ms p(95)=29.87ms p(99.9)=49.27ms
     iterations.....................: 302046  2512.785884/s
     success_rate...................: 100.00% ✓ 302046      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.28)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 877140      ✗ 0     
     data_received..................: 26 GB   213 MB/s
     data_sent......................: 352 MB  2.9 MB/s
     http_req_blocked...............: avg=3.25µs   min=791ns   med=2.29µs  max=17.56ms  p(90)=4.23µs  p(95)=5.02µs  p(99.9)=35.51µs 
     http_req_connecting............: avg=322ns    min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=20.28ms  min=1.77ms  med=17.88ms max=290.38ms p(90)=31.96ms p(95)=38.39ms p(99.9)=114.6ms 
       { expected_response:true }...: avg=20.28ms  min=1.77ms  med=17.88ms max=290.38ms p(90)=31.96ms p(95)=38.39ms p(99.9)=114.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 292480
     http_req_receiving.............: avg=659.67µs min=51.37µs med=98.47µs max=134.27ms p(90)=1.41ms  p(95)=2.47ms  p(99.9)=27.1ms  
     http_req_sending...............: avg=43.75µs  min=4.69µs  med=9.02µs  max=110.52ms p(90)=19.11µs p(95)=90.64µs p(99.9)=3.94ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=19.58ms  min=1.63ms  med=17.25ms max=290.05ms p(90)=30.89ms p(95)=37.11ms p(99.9)=112.76ms
     http_reqs......................: 292480  2432.784274/s
     iteration_duration.............: avg=20.51ms  min=2.77ms  med=18.08ms max=306.04ms p(90)=32.2ms  p(95)=38.65ms p(99.9)=115ms   
     iterations.....................: 292380  2431.952496/s
     success_rate...................: 100.00% ✓ 292380      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: grafbase (HotChocolate subgraphs) (0.53.5)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 583467      ✗ 0     
     data_received..................: 17 GB   142 MB/s
     data_sent......................: 234 MB  1.9 MB/s
     http_req_blocked...............: avg=3.32µs  min=771ns   med=2.21µs  max=4.21ms   p(90)=4.57µs   p(95)=5.74µs   p(99.9)=43.07µs
     http_req_connecting............: avg=492ns   min=0s      med=0s      max=4.17ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=30.6ms  min=2.26ms  med=30.15ms max=308.16ms p(90)=40.44ms  p(95)=43.74ms  p(99.9)=64.74ms
       { expected_response:true }...: avg=30.6ms  min=2.26ms  med=30.15ms max=308.16ms p(90)=40.44ms  p(95)=43.74ms  p(99.9)=64.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 194589
     http_req_receiving.............: avg=96.06µs min=28.08µs med=54.61µs max=130.8ms  p(90)=126.73µs p(95)=212.36µs p(99.9)=4.29ms 
     http_req_sending...............: avg=43.04µs min=4.29µs  med=9.3µs   max=225.37ms p(90)=23.45µs  p(95)=110.51µs p(99.9)=3.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=30.46ms min=2.09ms  med=30.02ms max=295.33ms p(90)=40.28ms  p(95)=43.56ms  p(99.9)=63.94ms
     http_reqs......................: 194589  1617.464738/s
     iteration_duration.............: avg=30.84ms min=5.08ms  med=30.37ms max=320.54ms p(90)=40.65ms  p(95)=43.96ms  p(99.9)=65.49ms
     iterations.....................: 194489  1616.633517/s
     success_rate...................: 100.00% ✓ 194489      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.359.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 513756      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 206 MB  1.7 MB/s
     http_req_blocked...............: avg=3.27µs  min=861ns   med=2.33µs  max=4.03ms   p(90)=4.03µs   p(95)=4.79µs  p(99.9)=35.21µs
     http_req_connecting............: avg=575ns   min=0s      med=0s      max=4ms      p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=34.79ms min=2.53ms  med=33.87ms max=289.31ms p(90)=49.6ms   p(95)=54.55ms p(99.9)=79.37ms
       { expected_response:true }...: avg=34.79ms min=2.53ms  med=33.87ms max=289.31ms p(90)=49.6ms   p(95)=54.55ms p(99.9)=79.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 171352
     http_req_receiving.............: avg=79.01µs min=24.22µs med=59.65µs max=178ms    p(90)=100.45µs p(95)=120.5µs p(99.9)=1.4ms  
     http_req_sending...............: avg=27.19µs min=4.67µs  med=10.81µs max=148.24ms p(90)=18.19µs  p(95)=22.89µs p(99.9)=1.2ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=34.69ms min=2.44ms  med=33.77ms max=285.08ms p(90)=49.5ms   p(95)=54.42ms p(99.9)=78.86ms
     http_reqs......................: 171352  1424.023224/s
     iteration_duration.............: avg=35.03ms min=4.09ms  med=34.08ms max=310.34ms p(90)=49.81ms  p(95)=54.76ms p(99.9)=79.7ms 
     iterations.....................: 171252  1423.192173/s
     success_rate...................: 100.00% ✓ 171252      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 483738      ✗ 0     
     data_received..................: 14 GB   117 MB/s
     data_sent......................: 194 MB  1.6 MB/s
     http_req_blocked...............: avg=3.3µs   min=781ns  med=2.42µs  max=4.14ms   p(90)=4.08µs   p(95)=4.8µs    p(99.9)=30.08µs
     http_req_connecting............: avg=560ns   min=0s     med=0s      max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.96ms min=2.56ms med=35.86ms max=309.06ms p(90)=52.63ms  p(95)=58.05ms  p(99.9)=87.99ms
       { expected_response:true }...: avg=36.96ms min=2.56ms med=35.86ms max=309.06ms p(90)=52.63ms  p(95)=58.05ms  p(99.9)=87.99ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161346
     http_req_receiving.............: avg=79.28µs min=27.4µs med=62.29µs max=248.05ms p(90)=100.79µs p(95)=118.46µs p(99.9)=1.25ms 
     http_req_sending...............: avg=25.75µs min=4.65µs med=11.48µs max=189.56ms p(90)=19.2µs   p(95)=22.91µs  p(99.9)=1.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.85ms min=2.47ms med=35.77ms max=295.07ms p(90)=52.52ms  p(95)=57.93ms  p(99.9)=87.65ms
     http_reqs......................: 161346  1341.016118/s
     iteration_duration.............: avg=37.2ms  min=5.31ms med=36.08ms max=329.52ms p(90)=52.85ms  p(95)=58.28ms  p(99.9)=88.52ms
     iterations.....................: 161246  1340.184975/s
     success_rate...................: 100.00% ✓ 161246      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 185895     ✗ 0    
     data_received..................: 5.4 GB  45 MB/s
     data_sent......................: 75 MB   618 kB/s
     http_req_blocked...............: avg=4.24µs  min=1.17µs  med=3.28µs  max=2.25ms   p(90)=4.73µs   p(95)=5.4µs    p(99.9)=52.43µs 
     http_req_connecting............: avg=719ns   min=0s      med=0s      max=2.23ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.45ms min=4.45ms  med=90.98ms max=324.71ms p(90)=139.41ms p(95)=153.94ms p(99.9)=259.62ms
       { expected_response:true }...: avg=96.45ms min=4.45ms  med=90.98ms max=324.71ms p(90)=139.41ms p(95)=153.94ms p(99.9)=259.62ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 62065
     http_req_receiving.............: avg=89.8µs  min=30.65µs med=75.73µs max=107.62ms p(90)=109.35µs p(95)=121.62µs p(99.9)=654.77µs
     http_req_sending...............: avg=25.39µs min=5.23µs  med=14.88µs max=115.44ms p(90)=20.97µs  p(95)=23.16µs  p(99.9)=594.66µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.33ms min=4.35ms  med=90.84ms max=324.6ms  p(90)=139.3ms  p(95)=153.8ms  p(99.9)=259.55ms
     http_reqs......................: 62065   514.564357/s
     iteration_duration.............: avg=96.84ms min=20.92ms med=91.39ms max=325ms    p(90)=139.68ms p(95)=154.25ms p(99.9)=260.95ms
     iterations.....................: 61965   513.735284/s
     success_rate...................: 100.00% ✓ 61965      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.18.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 163632     ✗ 0    
     data_received..................: 4.8 GB  40 MB/s
     data_sent......................: 66 MB   544 kB/s
     http_req_blocked...............: avg=5.71µs   min=1.22µs  med=3.7µs    max=4.28ms   p(90)=5.31µs   p(95)=5.93µs   p(99.9)=60.6µs  
     http_req_connecting............: avg=1.74µs   min=0s      med=0s       max=4.23ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=109.55ms min=5.24ms  med=107.48ms max=324.96ms p(90)=144.52ms p(95)=155.44ms p(99.9)=197.25ms
       { expected_response:true }...: avg=109.55ms min=5.24ms  med=107.48ms max=324.96ms p(90)=144.52ms p(95)=155.44ms p(99.9)=197.25ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 54644
     http_req_receiving.............: avg=89.56µs  min=31.08µs med=84.17µs  max=57.4ms   p(90)=114.22µs p(95)=126.36µs p(99.9)=561.93µs
     http_req_sending...............: avg=24.44µs  min=5.71µs  med=17.5µs   max=50.96ms  p(90)=22.72µs  p(95)=24.69µs  p(99.9)=581.19µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=109.43ms min=5.14ms  med=107.36ms max=324.32ms p(90)=144.41ms p(95)=155.32ms p(99.9)=196.93ms
     http_reqs......................: 54644   452.922172/s
     iteration_duration.............: avg=110.03ms min=29.57ms med=107.8ms  max=333.87ms p(90)=144.84ms p(95)=155.78ms p(99.9)=199.17ms
     iterations.....................: 54544   452.093312/s
     success_rate...................: 100.00% ✓ 54544      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-v3 (HotChocolate subgraphs) (v3.0.0-preview.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 143454     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   477 kB/s
     http_req_blocked...............: avg=8.68µs   min=1.1µs   med=3.22µs   max=8.62ms   p(90)=4.68µs   p(95)=5.25µs   p(99.9)=841.51µs
     http_req_connecting............: avg=4.87µs   min=0s      med=0s       max=8.56ms   p(90)=0s       p(95)=0s       p(99.9)=409.63µs
     http_req_duration..............: avg=124.98ms min=5.88ms  med=122.5ms  max=318.58ms p(90)=163.53ms p(95)=176.59ms p(99.9)=225.49ms
       { expected_response:true }...: avg=124.98ms min=5.88ms  med=122.5ms  max=318.58ms p(90)=163.53ms p(95)=176.59ms p(99.9)=225.49ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 47918
     http_req_receiving.............: avg=85.57µs  min=28.96µs med=83.9µs   max=9.24ms   p(90)=113.43µs p(95)=124.89µs p(99.9)=557.09µs
     http_req_sending...............: avg=22.6µs   min=5.11µs  med=16.82µs  max=73.46ms  p(90)=21.67µs  p(95)=23.36µs  p(99.9)=952.17µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=124.87ms min=5.74ms  med=122.39ms max=317.27ms p(90)=163.42ms p(95)=176.48ms p(99.9)=225.29ms
     http_reqs......................: 47918   396.969553/s
     iteration_duration.............: avg=125.51ms min=26.2ms  med=122.81ms max=333.82ms p(90)=163.84ms p(95)=176.9ms  p(99.9)=227.97ms
     iterations.....................: 47818   396.141118/s
     success_rate...................: 100.00% ✓ 47818      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-gateway (HotChocolate subgraphs) (2.14.4)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 97452      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 39 MB   323 kB/s
     http_req_blocked...............: avg=6.59µs   min=1.13µs  med=3.11µs   max=3.76ms   p(90)=4.42µs   p(95)=4.96µs   p(99.9)=1.79ms  
     http_req_connecting............: avg=3.25µs   min=0s      med=0s       max=3.73ms   p(90)=0s       p(95)=0s       p(99.9)=1.68ms  
     http_req_duration..............: avg=183.97ms min=7.49ms  med=183.3ms  max=338.41ms p(90)=197.53ms p(95)=203.2ms  p(99.9)=272.36ms
       { expected_response:true }...: avg=183.97ms min=7.49ms  med=183.3ms  max=338.41ms p(90)=197.53ms p(95)=203.2ms  p(99.9)=272.36ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32584
     http_req_receiving.............: avg=90.65µs  min=30.37µs med=86.93µs  max=61.58ms  p(90)=116.53µs p(95)=127.42µs p(99.9)=369.74µs
     http_req_sending...............: avg=22.11µs  min=5.02µs  med=16.15µs  max=70.24ms  p(90)=20.53µs  p(95)=22.28µs  p(99.9)=577.98µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.85ms min=7.4ms   med=183.19ms max=337.76ms p(90)=197.42ms p(95)=203.09ms p(99.9)=271.95ms
     http_reqs......................: 32584   269.37016/s
     iteration_duration.............: avg=184.81ms min=39.77ms med=183.59ms max=368.09ms p(90)=197.8ms  p(95)=203.51ms p(99.9)=276.56ms
     iterations.....................: 32484   268.543466/s
     success_rate...................: 100.00% ✓ 32484      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 96873      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   321 kB/s
     http_req_blocked...............: avg=10.7µs   min=1.05µs  med=3.34µs   max=8.43ms   p(90)=4.72µs   p(95)=5.31µs   p(99.9)=3.43ms  
     http_req_connecting............: avg=6.98µs   min=0s      med=0s       max=8.28ms   p(90)=0s       p(95)=0s       p(99.9)=3.12ms  
     http_req_duration..............: avg=185.2ms  min=5.9ms   med=167.26ms max=805.11ms p(90)=211.26ms p(95)=244.74ms p(99.9)=711.84ms
       { expected_response:true }...: avg=185.2ms  min=5.9ms   med=167.26ms max=805.11ms p(90)=211.26ms p(95)=244.74ms p(99.9)=711.84ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32391
     http_req_receiving.............: avg=92.76µs  min=30.76µs med=89.88µs  max=24.18ms  p(90)=119.82µs p(95)=131.47µs p(99.9)=676.58µs
     http_req_sending...............: avg=26.26µs  min=5.58µs  med=17.21µs  max=30.01ms  p(90)=21.51µs  p(95)=23.22µs  p(99.9)=2.01ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=185.08ms min=5.8ms   med=167.13ms max=804.72ms p(90)=211.12ms p(95)=244.6ms  p(99.9)=711.66ms
     http_reqs......................: 32391   267.567659/s
     iteration_duration.............: avg=186.02ms min=63.22ms med=167.59ms max=805.36ms p(90)=211.64ms p(95)=245.31ms p(99.9)=712.5ms 
     iterations.....................: 32291   266.741604/s
     success_rate...................: 100.00% ✓ 32291      ✗ 0    
     vus............................: 7       min=7        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

