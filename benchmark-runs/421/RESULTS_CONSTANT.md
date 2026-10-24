## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-fed-net-11 | 16.7.0-p.38 | 3,592 | 3,957 | 3,495 | 3.9% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.38 | 3,572 | 3,936 | 3,531 | 3.6% |  |
| fusion-nightly-net-11 | 16.7.0-p.38 | 3,528 | 3,867 | 3,475 | 3.6% |  |
| fusion-nightly-net-10 | 16.7.0-p.38 | 3,522 | 3,830 | 3,481 | 3.1% |  |
| fusion-nightly-fed-aot-11 | 16.7.0-p.38 | 3,472 | 3,760 | 3,456 | 2.9% |  |
| fusion-nightly-aot-11 | 16.7.0-p.38 | 3,468 | 3,757 | 3,417 | 3.3% |  |
| feddi-gateway | 3c75a7db8876 | 3,130 | 3,339 | 3,083 | 2.6% |  |
| hive-router | v0.3.5 | 2,680 | 2,807 | 2,643 | 1.9% |  |
| fusion-net-11 | 16.6.9 | 2,562 | 2,672 | 2,540 | 1.7% |  |
| fusion-net-10 | 16.6.9 | 2,525 | 2,631 | 2,501 | 1.8% |  |
| fusion-fed-net-11 | 16.6.9 | 2,377 | 2,462 | 2,361 | 1.5% |  |
| fusion-fed-net-10 | 16.6.9 | 2,336 | 2,444 | 2,320 | 1.9% |  |
| fusion-aot-11 | 16.6.9 | 2,122 | 2,207 | 2,111 | 1.6% |  |
| fusion-fed-aot-11 | 16.6.9 | 1,968 | 2,050 | 1,957 | 1.7% |  |
| grafbase | 0.53.5 | 1,657 | 1,726 | 1,650 | 1.6% |  |
| caliban | 3.2.0 | 1,444 | 1,494 | 1,429 | 1.5% |  |
| cosmo | 0.361.0 | 1,432 | 1,485 | 1,424 | 1.6% |  |
| hive-gateway-router-runtime | 2.15.2 | 507 | 525 | 505 | 1.5% |  |
| apollo-router | v2.18.0 | 433 | 447 | 430 | 1.3% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 410 | 419 | 393 | 1.9% |  |
| hive-gateway | 2.15.2 | 265 | 274 | 262 | 1.4% |  |
| apollo-gateway | 2.14.4 | 263 | 270 | 261 | 1.1% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1294911     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=3.36µs   min=881ns   med=2.39µs  max=27.62ms  p(90)=3.79µs   p(95)=4.51µs  p(99.9)=33.39µs
     http_req_connecting............: avg=199ns    min=0s      med=0s      max=3.41ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.66ms  min=1.21ms  med=12.38ms max=289.21ms p(90)=21.57ms  p(95)=25.7ms  p(99.9)=51.34ms
       { expected_response:true }...: avg=13.66ms  min=1.21ms  med=12.38ms max=289.21ms p(90)=21.57ms  p(95)=25.7ms  p(99.9)=51.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431737
     http_req_receiving.............: avg=552.68µs min=53.24µs med=81.69µs max=188.49ms p(90)=953.24µs p(95)=2.84ms  p(99.9)=26.47ms
     http_req_sending...............: avg=62.23µs  min=4.48µs  med=8.52µs  max=187.52ms p(90)=15.45µs  p(95)=99.32µs p(99.9)=9.89ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.05ms  min=1.11ms  med=11.75ms max=288.47ms p(90)=20.78ms  p(95)=24.66ms p(99.9)=49.31ms
     http_reqs......................: 431737  3592.62445/s
     iteration_duration.............: avg=13.89ms  min=1.64ms  med=12.58ms max=299.65ms p(90)=21.81ms  p(95)=25.99ms p(99.9)=52.18ms
     iterations.....................: 431637  3591.792318/s
     success_rate...................: 100.00% ✓ 431637      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1287687     ✗ 0     
     data_received..................: 38 GB   313 MB/s
     data_sent......................: 516 MB  4.3 MB/s
     http_req_blocked...............: avg=4.48µs   min=971ns   med=2.46µs  max=158.38ms p(90)=3.95µs  p(95)=4.72µs   p(99.9)=33.95µs
     http_req_connecting............: avg=1.41µs   min=0s      med=0s      max=157.91ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=13.74ms  min=1.23ms  med=12.46ms max=286.04ms p(90)=21.67ms p(95)=25.87ms  p(99.9)=52.03ms
       { expected_response:true }...: avg=13.74ms  min=1.23ms  med=12.46ms max=286.04ms p(90)=21.67ms p(95)=25.87ms  p(99.9)=52.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429329
     http_req_receiving.............: avg=688.27µs min=52.12µs med=84.13µs max=132.52ms p(90)=1.73ms  p(95)=3.79ms   p(99.9)=27.75ms
     http_req_sending...............: avg=65.18µs  min=4.61µs  med=8.85µs  max=131.52ms p(90)=16.27µs p(95)=101.64µs p(99.9)=10.71ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=12.98ms  min=1.16ms  med=11.69ms max=257.46ms p(90)=20.72ms p(95)=24.69ms  p(99.9)=49.78ms
     http_reqs......................: 429329  3572.774235/s
     iteration_duration.............: avg=13.96ms  min=1.72ms  med=12.67ms max=296.11ms p(90)=21.9ms  p(95)=26.14ms  p(99.9)=52.76ms
     iterations.....................: 429229  3571.942058/s
     success_rate...................: 100.00% ✓ 429229      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1271343     ✗ 0     
     data_received..................: 37 GB   309 MB/s
     data_sent......................: 509 MB  4.2 MB/s
     http_req_blocked...............: avg=3.36µs   min=811ns    med=2.42µs  max=22.1ms   p(90)=3.74µs  p(95)=4.4µs   p(99.9)=34.86µs
     http_req_connecting............: avg=213ns    min=0s       med=0s      max=4.05ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.92ms  min=910.67µs med=12.63ms max=270.02ms p(90)=21.87ms p(95)=26.1ms  p(99.9)=52.19ms
       { expected_response:true }...: avg=13.92ms  min=910.67µs med=12.63ms max=270.02ms p(90)=21.87ms p(95)=26.1ms  p(99.9)=52.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 423881
     http_req_receiving.............: avg=688.75µs min=51.43µs  med=82.03µs max=170.93ms p(90)=1.52ms  p(95)=3.92ms  p(99.9)=28.16ms
     http_req_sending...............: avg=61.45µs  min=4.5µs    med=8.67µs  max=123.59ms p(90)=15.15µs p(95)=97.29µs p(99.9)=10.2ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.17ms  min=796.32µs med=11.89ms max=269.55ms p(90)=20.86ms p(95)=24.76ms p(99.9)=49.22ms
     http_reqs......................: 423881  3528.766647/s
     iteration_duration.............: avg=14.14ms  min=1.29ms   med=12.83ms max=290.11ms p(90)=22.11ms p(95)=26.39ms p(99.9)=53.21ms
     iterations.....................: 423781  3527.934157/s
     success_rate...................: 100.00% ✓ 423781      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1269387     ✗ 0     
     data_received..................: 37 GB   309 MB/s
     data_sent......................: 509 MB  4.2 MB/s
     http_req_blocked...............: avg=3.15µs   min=902ns    med=2.38µs  max=21.26ms  p(90)=3.74µs  p(95)=4.41µs  p(99.9)=32.91µs
     http_req_connecting............: avg=242ns    min=0s       med=0s      max=3.68ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.94ms  min=962.11µs med=12.68ms max=291.25ms p(90)=21.98ms p(95)=26.25ms p(99.9)=52.27ms
       { expected_response:true }...: avg=13.94ms  min=962.11µs med=12.68ms max=291.25ms p(90)=21.98ms p(95)=26.25ms p(99.9)=52.27ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 423229
     http_req_receiving.............: avg=843.54µs min=53.31µs  med=83.06µs max=173.45ms p(90)=2.23ms  p(95)=4.77ms  p(99.9)=31.18ms
     http_req_sending...............: avg=61.5µs   min=4.58µs   med=8.71µs  max=61.25ms  p(90)=15.39µs p(95)=96.99µs p(99.9)=10.45ms
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.04ms  min=856.64µs med=11.77ms max=290.84ms p(90)=20.76ms p(95)=24.71ms p(99.9)=49.62ms
     http_reqs......................: 423229  3522.85243/s
     iteration_duration.............: avg=14.17ms  min=1.49ms   med=12.89ms max=318.54ms p(90)=22.22ms p(95)=26.56ms p(99.9)=53.18ms
     iterations.....................: 423129  3522.020055/s
     success_rate...................: 100.00% ✓ 423129      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1251426     ✗ 0     
     data_received..................: 37 GB   304 MB/s
     data_sent......................: 501 MB  4.2 MB/s
     http_req_blocked...............: avg=5.95µs   min=1µs     med=2.5µs   max=233.96ms p(90)=3.99µs  p(95)=4.74µs   p(99.9)=36.05µs
     http_req_connecting............: avg=2.68µs   min=0s      med=0s      max=233.82ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.14ms  min=1.32ms  med=12.96ms max=273.5ms  p(90)=21.46ms p(95)=25.44ms  p(99.9)=50.2ms 
       { expected_response:true }...: avg=14.14ms  min=1.32ms  med=12.96ms max=273.5ms  p(90)=21.46ms p(95)=25.44ms  p(99.9)=50.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 417242
     http_req_receiving.............: avg=822.96µs min=52.81µs med=86.9µs  max=112.38ms p(90)=2.36ms  p(95)=4.04ms   p(99.9)=27.23ms
     http_req_sending...............: avg=62.5µs   min=4.84µs  med=9.17µs  max=77.34ms  p(90)=16.9µs  p(95)=105.13µs p(99.9)=9.53ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.26ms  min=1.22ms  med=12.02ms max=273.22ms p(90)=20.39ms p(95)=24.23ms  p(99.9)=47.89ms
     http_reqs......................: 417242  3472.124495/s
     iteration_duration.............: avg=14.37ms  min=1.79ms  med=13.17ms max=323.85ms p(90)=21.69ms p(95)=25.72ms  p(99.9)=51.11ms
     iterations.....................: 417142  3471.292334/s
     success_rate...................: 100.00% ✓ 417142      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.7.0-p.38)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1249809     ✗ 0     
     data_received..................: 37 GB   304 MB/s
     data_sent......................: 501 MB  4.2 MB/s
     http_req_blocked...............: avg=2.78µs  min=821ns    med=1.95µs  max=24.62ms  p(90)=3.19µs  p(95)=3.89µs  p(99.9)=26.46µs
     http_req_connecting............: avg=208ns   min=0s       med=0s      max=3.43ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.17ms min=1ms      med=13.01ms max=281.61ms p(90)=21.46ms p(95)=25.75ms p(99.9)=50.33ms
       { expected_response:true }...: avg=14.17ms min=1ms      med=13.01ms max=281.61ms p(90)=21.46ms p(95)=25.75ms p(99.9)=50.33ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 416703
     http_req_receiving.............: avg=1.01ms  min=49.48µs  med=82.23µs max=57.95ms  p(90)=3.17ms  p(95)=5.44ms  p(99.9)=29.55ms
     http_req_sending...............: avg=59.5µs  min=4.33µs   med=8.05µs  max=214.14ms p(90)=14.78µs p(95)=88.62µs p(99.9)=11.42ms
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.1ms  min=868.51µs med=11.93ms max=280.97ms p(90)=19.98ms p(95)=23.93ms p(99.9)=47.06ms
     http_reqs......................: 416703  3468.255814/s
     iteration_duration.............: avg=14.39ms min=1.56ms   med=13.2ms  max=291.73ms p(90)=21.68ms p(95)=26.01ms p(99.9)=51.38ms
     iterations.....................: 416603  3467.423505/s
     success_rate...................: 100.00% ✓ 416603      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1128003     ✗ 0     
     data_received..................: 33 GB   274 MB/s
     data_sent......................: 452 MB  3.8 MB/s
     http_req_blocked...............: avg=3.13µs  min=842ns    med=2.36µs  max=18.2ms   p(90)=3.9µs   p(95)=4.66µs   p(99.9)=37.41µs
     http_req_connecting............: avg=232ns   min=0s       med=0s      max=3.52ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.73ms min=1.02ms   med=15.45ms max=308.74ms p(90)=23.83ms p(95)=26.99ms  p(99.9)=48.25ms
       { expected_response:true }...: avg=15.73ms min=1.02ms   med=15.45ms max=308.74ms p(90)=23.83ms p(95)=26.99ms  p(99.9)=48.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 376101
     http_req_receiving.............: avg=99.58µs min=24.31µs  med=49.75µs max=128.27ms p(90)=97.23µs p(95)=205.73µs p(99.9)=7.44ms 
     http_req_sending...............: avg=53.77µs min=4.65µs   med=9.49µs  max=144.2ms  p(90)=16.53µs p(95)=110.68µs p(99.9)=6.33ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.58ms min=955.33µs med=15.32ms max=308.18ms p(90)=23.64ms p(95)=26.73ms  p(99.9)=47.13ms
     http_reqs......................: 376101  3130.465916/s
     iteration_duration.............: avg=15.94ms min=1.53ms   med=15.64ms max=344.37ms p(90)=24.03ms p(95)=27.21ms  p(99.9)=49.22ms
     iterations.....................: 376001  3129.633569/s
     success_rate...................: 100.00% ✓ 376001      ✗ 0     
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

     checks.........................: 100.00% ✓ 966294      ✗ 0     
     data_received..................: 28 GB   234 MB/s
     data_sent......................: 387 MB  3.2 MB/s
     http_req_blocked...............: avg=3.54µs   min=1.03µs  med=2.78µs  max=7.1ms    p(90)=4.56µs  p(95)=5.4µs    p(99.9)=43.38µs
     http_req_connecting............: avg=314ns    min=0s      med=0s      max=4.21ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=18.39ms  min=1.62ms  med=17.91ms max=292.96ms p(90)=25.57ms p(95)=28.49ms  p(99.9)=49.24ms
       { expected_response:true }...: avg=18.39ms  min=1.62ms  med=17.91ms max=292.96ms p(90)=25.57ms p(95)=28.49ms  p(99.9)=49.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 322198
     http_req_receiving.............: avg=104.03µs min=27.08µs med=52.01µs max=101.21ms p(90)=98.67µs p(95)=182.65µs p(99.9)=8.71ms 
     http_req_sending...............: avg=51.32µs  min=4.79µs  med=10.43µs max=85.27ms  p(90)=19.07µs p(95)=109.76µs p(99.9)=5.97ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=18.23ms  min=1.52ms  med=17.78ms max=292.62ms p(90)=25.39ms p(95)=28.21ms  p(99.9)=48.26ms
     http_reqs......................: 322198  2680.315301/s
     iteration_duration.............: avg=18.61ms  min=2.62ms  med=18.11ms max=320.48ms p(90)=25.79ms p(95)=28.74ms  p(99.9)=49.96ms
     iterations.....................: 322098  2679.483416/s
     success_rate...................: 100.00% ✓ 322098      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 923610      ✗ 0     
     data_received..................: 27 GB   225 MB/s
     data_sent......................: 370 MB  3.1 MB/s
     http_req_blocked...............: avg=3.61µs  min=1µs     med=2.51µs  max=20.83ms  p(90)=4.23µs  p(95)=5.11µs   p(99.9)=38.42µs
     http_req_connecting............: avg=291ns   min=0s      med=0s      max=3.47ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.25ms min=1.49ms  med=18.54ms max=324.27ms p(90)=26.09ms p(95)=29.38ms  p(99.9)=53.05ms
       { expected_response:true }...: avg=19.25ms min=1.49ms  med=18.54ms max=324.27ms p(90)=26.09ms p(95)=29.38ms  p(99.9)=53.05ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 307970
     http_req_receiving.............: avg=2.04ms  min=51.58µs med=1.54ms  max=300.75ms p(90)=4.39ms  p(95)=5.94ms   p(99.9)=29.78ms
     http_req_sending...............: avg=50.7µs  min=4.68µs  med=9.42µs  max=36.91ms  p(90)=19.69µs p(95)=103.55µs p(99.9)=5.74ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.16ms min=1.38ms  med=16.39ms max=83.76ms  p(90)=23.39ms p(95)=26.54ms  p(99.9)=48.26ms
     http_reqs......................: 307970  2562.441819/s
     iteration_duration.............: avg=19.47ms min=2.4ms   med=18.75ms max=363.77ms p(90)=26.3ms  p(95)=29.62ms  p(99.9)=53.42ms
     iterations.....................: 307870  2561.609777/s
     success_rate...................: 100.00% ✓ 307870      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 910248      ✗ 0     
     data_received..................: 27 GB   221 MB/s
     data_sent......................: 365 MB  3.0 MB/s
     http_req_blocked...............: avg=3.07µs  min=852ns   med=2.01µs  max=15.87ms  p(90)=3.65µs  p(95)=4.43µs  p(99.9)=27.63µs
     http_req_connecting............: avg=410ns   min=0s      med=0s      max=4.59ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.54ms min=1.57ms  med=18.96ms max=306.57ms p(90)=26.43ms p(95)=29.34ms p(99.9)=49.76ms
       { expected_response:true }...: avg=19.54ms min=1.57ms  med=18.96ms max=306.57ms p(90)=26.43ms p(95)=29.34ms p(99.9)=49.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 303516
     http_req_receiving.............: avg=1.47ms  min=51.09µs med=1.05ms  max=168.57ms p(90)=3.3ms   p(95)=4.33ms  p(99.9)=25.43ms
     http_req_sending...............: avg=45.75µs min=4.67µs  med=8.43µs  max=121.69ms p(90)=18.38µs p(95)=90.26µs p(99.9)=5.04ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=18.02ms min=1.47ms  med=17.4ms  max=295.57ms p(90)=24.72ms p(95)=27.59ms p(99.9)=46.94ms
     http_reqs......................: 303516  2525.11746/s
     iteration_duration.............: avg=19.76ms min=2.47ms  med=19.16ms max=318.71ms p(90)=26.64ms p(95)=29.58ms p(99.9)=50.48ms
     iterations.....................: 303416  2524.285504/s
     success_rate...................: 100.00% ✓ 303416      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 857241      ✗ 0     
     data_received..................: 25 GB   208 MB/s
     data_sent......................: 344 MB  2.9 MB/s
     http_req_blocked...............: avg=3.12µs  min=882ns   med=2.17µs  max=13.31ms  p(90)=4.01µs  p(95)=4.91µs   p(99.9)=29.55µs
     http_req_connecting............: avg=306ns   min=0s      med=0s      max=3.55ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=20.75ms min=1.74ms  med=20.14ms max=265.87ms p(90)=27.28ms p(95)=30.2ms   p(99.9)=53.52ms
       { expected_response:true }...: avg=20.75ms min=1.74ms  med=20.14ms max=265.87ms p(90)=27.28ms p(95)=30.2ms   p(99.9)=53.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 285847
     http_req_receiving.............: avg=2.23ms  min=51.36µs med=1.98ms  max=146.19ms p(90)=4.47ms  p(95)=5.92ms   p(99.9)=28.86ms
     http_req_sending...............: avg=49.42µs min=4.7µs   med=8.82µs  max=153.36ms p(90)=20.94µs p(95)=100.33µs p(99.9)=5.42ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=18.47ms min=1.67ms  med=17.8ms  max=265.36ms p(90)=24.4ms  p(95)=27.13ms  p(99.9)=48.46ms
     http_reqs......................: 285847  2377.682389/s
     iteration_duration.............: avg=20.98ms min=2.76ms  med=20.35ms max=296.22ms p(90)=27.49ms p(95)=30.43ms  p(99.9)=54.14ms
     iterations.....................: 285747  2376.850587/s
     success_rate...................: 100.00% ✓ 285747      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-10 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 842400      ✗ 0     
     data_received..................: 25 GB   205 MB/s
     data_sent......................: 338 MB  2.8 MB/s
     http_req_blocked...............: avg=3.85µs  min=1.09µs  med=2.76µs   max=19.89ms  p(90)=4.52µs  p(95)=5.36µs   p(99.9)=37.42µs
     http_req_connecting............: avg=359ns   min=0s      med=0s       max=4.16ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=21.08ms min=1.87ms  med=20.35ms  max=300.07ms p(90)=28.92ms p(95)=32.26ms  p(99.9)=53.65ms
       { expected_response:true }...: avg=21.08ms min=1.87ms  med=20.35ms  max=300.07ms p(90)=28.92ms p(95)=32.26ms  p(99.9)=53.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280900
     http_req_receiving.............: avg=1.53ms  min=53.63µs med=979.39µs max=184.03ms p(90)=3.58ms  p(95)=4.82ms   p(99.9)=26.56ms
     http_req_sending...............: avg=49.05µs min=5.07µs  med=10.18µs  max=82.52ms  p(90)=20.35µs p(95)=107.71µs p(99.9)=4.19ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.49ms min=1.76ms  med=18.72ms  max=299.83ms p(90)=27.13ms p(95)=30.45ms  p(99.9)=50.54ms
     http_reqs......................: 280900  2336.211952/s
     iteration_duration.............: avg=21.35ms min=2.94ms  med=20.6ms   max=311.65ms p(90)=29.18ms p(95)=32.54ms  p(99.9)=54.62ms
     iterations.....................: 280800  2335.380264/s
     success_rate...................: 100.00% ✓ 280800      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 765249      ✗ 0     
     data_received..................: 22 GB   186 MB/s
     data_sent......................: 307 MB  2.6 MB/s
     http_req_blocked...............: avg=2.92µs  min=801ns   med=2.03µs  max=16.42ms  p(90)=3.73µs  p(95)=4.53µs  p(99.9)=27.39µs
     http_req_connecting............: avg=351ns   min=0s      med=0s      max=3.55ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=23.28ms min=1.66ms  med=22.69ms max=289.99ms p(90)=29.86ms p(95)=32.71ms p(99.9)=53.88ms
       { expected_response:true }...: avg=23.28ms min=1.66ms  med=22.69ms max=289.99ms p(90)=29.86ms p(95)=32.71ms p(99.9)=53.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 255183
     http_req_receiving.............: avg=2.82ms  min=53.21µs med=2.77ms  max=64.62ms  p(90)=4.88ms  p(95)=6.02ms  p(99.9)=28.12ms
     http_req_sending...............: avg=45.09µs min=4.66µs  med=8.66µs  max=186.46ms p(90)=19.93µs p(95)=89.87µs p(99.9)=4.68ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=20.41ms min=1.54ms  med=19.76ms max=289.35ms p(90)=26.64ms p(95)=29.31ms p(99.9)=48.28ms
     http_reqs......................: 255183  2122.883065/s
     iteration_duration.............: avg=23.51ms min=2.43ms  med=22.9ms  max=306.51ms p(90)=30.07ms p(95)=32.95ms p(99.9)=54.46ms
     iterations.....................: 255083  2122.051159/s
     success_rate...................: 100.00% ✓ 255083      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 709707      ✗ 0     
     data_received..................: 21 GB   173 MB/s
     data_sent......................: 284 MB  2.4 MB/s
     http_req_blocked...............: avg=2.86µs  min=872ns   med=2.14µs  max=3.66ms   p(90)=4.02µs  p(95)=4.8µs   p(99.9)=29.33µs
     http_req_connecting............: avg=247ns   min=0s      med=0s      max=2.62ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.12ms min=2.07ms  med=24.55ms max=282.04ms p(90)=31.58ms p(95)=34.46ms p(99.9)=56.57ms
       { expected_response:true }...: avg=25.12ms min=2.07ms  med=24.55ms max=282.04ms p(90)=31.58ms p(95)=34.46ms p(99.9)=56.57ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 236669
     http_req_receiving.............: avg=2.97ms  min=52.96µs med=2.93ms  max=221.03ms p(90)=5ms     p(95)=6.11ms  p(99.9)=28.05ms
     http_req_sending...............: avg=42.05µs min=4.36µs  med=8.61µs  max=193.01ms p(90)=19.68µs p(95)=84.61µs p(99.9)=3.91ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=22.1ms  min=1.9ms   med=21.48ms max=281.6ms  p(90)=28.15ms p(95)=30.87ms p(99.9)=50.83ms
     http_reqs......................: 236669  1968.114722/s
     iteration_duration.............: avg=25.35ms min=3.36ms  med=24.75ms max=292.92ms p(90)=31.8ms  p(95)=34.68ms p(99.9)=57.14ms
     iterations.....................: 236569  1967.283133/s
     success_rate...................: 100.00% ✓ 236569      ✗ 0     
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

     checks.........................: 100.00% ✓ 598074      ✗ 0     
     data_received..................: 18 GB   145 MB/s
     data_sent......................: 240 MB  2.0 MB/s
     http_req_blocked...............: avg=3.41µs  min=821ns   med=2.32µs  max=3.92ms   p(90)=4.73µs   p(95)=5.92µs   p(99.9)=43.4µs 
     http_req_connecting............: avg=465ns   min=0s      med=0s      max=3.87ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=29.84ms min=2.27ms  med=29.45ms max=297.22ms p(90)=38.86ms  p(95)=41.92ms  p(99.9)=62.65ms
       { expected_response:true }...: avg=29.84ms min=2.27ms  med=29.45ms max=297.22ms p(90)=38.86ms  p(95)=41.92ms  p(99.9)=62.65ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 199458
     http_req_receiving.............: avg=96.22µs min=28.04µs med=56.57µs max=146.62ms p(90)=125.58µs p(95)=195.83µs p(99.9)=3.84ms 
     http_req_sending...............: avg=44.78µs min=4.87µs  med=9.72µs  max=195.95ms p(90)=23.29µs  p(95)=106.18µs p(99.9)=3.24ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=29.7ms  min=2.2ms   med=29.33ms max=296.6ms  p(90)=38.71ms  p(95)=41.75ms  p(99.9)=61.51ms
     http_reqs......................: 199458  1657.923043/s
     iteration_duration.............: avg=30.09ms min=5.42ms  med=29.67ms max=312.99ms p(90)=39.09ms  p(95)=42.15ms  p(99.9)=63.29ms
     iterations.....................: 199358  1657.091829/s
     success_rate...................: 100.00% ✓ 199358      ✗ 0     
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

     checks.........................: 100.00% ✓ 521232      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=4.63µs  min=1.11µs  med=3.62µs  max=3.89ms   p(90)=5.63µs   p(95)=6.51µs   p(99.9)=44.82µs
     http_req_connecting............: avg=597ns   min=0s      med=0s      max=3.85ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.25ms min=2.42ms  med=33.32ms max=309.2ms  p(90)=48.37ms  p(95)=53.26ms  p(99.9)=79.04ms
       { expected_response:true }...: avg=34.25ms min=2.42ms  med=33.32ms max=309.2ms  p(90)=48.37ms  p(95)=53.26ms  p(99.9)=79.04ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 173844
     http_req_receiving.............: avg=93.7µs  min=29.78µs med=70.49µs max=141.81ms p(90)=116.54µs p(95)=142.02µs p(99.9)=2.37ms 
     http_req_sending...............: avg=36.67µs min=5.53µs  med=14.7µs  max=259.33ms p(90)=23.41µs  p(95)=29.39µs  p(99.9)=1.52ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.12ms min=2.3ms   med=33.21ms max=309.05ms p(90)=48.23ms  p(95)=53.1ms   p(99.9)=78.58ms
     http_reqs......................: 173844  1444.89378/s
     iteration_duration.............: avg=34.52ms min=5.81ms  med=33.57ms max=335.16ms p(90)=48.61ms  p(95)=53.53ms  p(99.9)=79.79ms
     iterations.....................: 173744  1444.062636/s
     success_rate...................: 100.00% ✓ 173744      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.361.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 516753      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.25µs  min=862ns   med=2.29µs  max=3.81ms   p(90)=3.94µs   p(95)=4.7µs    p(99.9)=32.89µs
     http_req_connecting............: avg=581ns   min=0s      med=0s      max=3.76ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.59ms min=2.28ms  med=33.66ms max=308.88ms p(90)=49.37ms  p(95)=54.3ms   p(99.9)=78.71ms
       { expected_response:true }...: avg=34.59ms min=2.28ms  med=33.66ms max=308.88ms p(90)=49.37ms  p(95)=54.3ms   p(99.9)=78.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 172351
     http_req_receiving.............: avg=80.31µs min=27.73µs med=62.49µs max=91.3ms   p(90)=104.28µs p(95)=123.86µs p(99.9)=1.14ms 
     http_req_sending...............: avg=27.98µs min=4.87µs  med=10.98µs max=168.98ms p(90)=18.44µs  p(95)=23.1µs   p(99.9)=1.17ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.48ms min=2.17ms  med=33.56ms max=308.35ms p(90)=49.25ms  p(95)=54.18ms  p(99.9)=78.54ms
     http_reqs......................: 172351  1432.746752/s
     iteration_duration.............: avg=34.82ms min=4.87ms  med=33.88ms max=321.35ms p(90)=49.58ms  p(95)=54.5ms   p(99.9)=79.34ms
     iterations.....................: 172251  1431.915456/s
     success_rate...................: 100.00% ✓ 172251      ✗ 0     
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

     checks.........................: 100.00% ✓ 183240     ✗ 0    
     data_received..................: 5.4 GB  44 MB/s
     data_sent......................: 74 MB   609 kB/s
     http_req_blocked...............: avg=5.03µs  min=1.26µs  med=3.29µs  max=3.76ms   p(90)=4.84µs   p(95)=5.51µs   p(99.9)=50.68µs 
     http_req_connecting............: avg=1.48µs  min=0s      med=0s      max=3.72ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=97.83ms min=4.5ms   med=94.87ms max=331.03ms p(90)=118.18ms p(95)=129.23ms p(99.9)=229.33ms
       { expected_response:true }...: avg=97.83ms min=4.5ms   med=94.87ms max=331.03ms p(90)=118.18ms p(95)=129.23ms p(99.9)=229.33ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61180
     http_req_receiving.............: avg=89.1µs  min=30.82µs med=77.91µs max=100.9ms  p(90)=111.84µs p(95)=124.34µs p(99.9)=729.29µs
     http_req_sending...............: avg=28.42µs min=5.43µs  med=15.4µs  max=132.76ms p(90)=21.23µs  p(95)=23.32µs  p(99.9)=665.58µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=97.72ms min=4.4ms   med=94.77ms max=330.44ms p(90)=118.07ms p(95)=129.09ms p(99.9)=228.51ms
     http_reqs......................: 61180   507.25269/s
     iteration_duration.............: avg=98.25ms min=28.88ms med=95.14ms max=364.09ms p(90)=118.45ms p(95)=129.55ms p(99.9)=231.25ms
     iterations.....................: 61080   506.423574/s
     success_rate...................: 100.00% ✓ 61080      ✗ 0    
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

     checks.........................: 100.00% ✓ 156450     ✗ 0    
     data_received..................: 4.6 GB  38 MB/s
     data_sent......................: 63 MB   520 kB/s
     http_req_blocked...............: avg=5.25µs   min=1.08µs  med=3.14µs   max=4.01ms   p(90)=4.61µs   p(95)=5.17µs   p(99.9)=135.37µs
     http_req_connecting............: avg=1.91µs   min=0s      med=0s       max=3.97ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=114.6ms  min=5.05ms  med=112.47ms max=322.22ms p(90)=151.58ms p(95)=163.27ms p(99.9)=211ms   
       { expected_response:true }...: avg=114.6ms  min=5.05ms  med=112.47ms max=322.22ms p(90)=151.58ms p(95)=163.27ms p(99.9)=211ms   
     http_req_failed................: 0.00%   ✓ 0          ✗ 52250
     http_req_receiving.............: avg=81.21µs  min=28.81µs med=78.14µs  max=14.03ms  p(90)=108.16µs p(95)=120.36µs p(99.9)=484.75µs
     http_req_sending...............: avg=26.71µs  min=5.27µs  med=15.85µs  max=125.13ms p(90)=20.93µs  p(95)=22.71µs  p(99.9)=454.49µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=114.49ms min=4.97ms  med=112.37ms max=321.95ms p(90)=151.47ms p(95)=163.13ms p(99.9)=210.75ms
     http_reqs......................: 52250   433.051065/s
     iteration_duration.............: avg=115.08ms min=30.53ms med=112.77ms max=336.53ms p(90)=151.89ms p(95)=163.56ms p(99.9)=212.96ms
     iterations.....................: 52150   432.222259/s
     success_rate...................: 100.00% ✓ 52150      ✗ 0    
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

     checks.........................: 100.00% ✓ 148257     ✗ 0    
     data_received..................: 4.3 GB  36 MB/s
     data_sent......................: 60 MB   493 kB/s
     http_req_blocked...............: avg=4.8µs    min=1.16µs  med=3.26µs   max=2.79ms   p(90)=4.82µs   p(95)=5.44µs   p(99.9)=120.37µs
     http_req_connecting............: avg=1.31µs   min=0s      med=0s       max=2.75ms   p(90)=0s       p(95)=0s       p(99.9)=54.64µs 
     http_req_duration..............: avg=120.92ms min=5.69ms  med=118.59ms max=323.5ms  p(90)=157.89ms p(95)=170.26ms p(99.9)=221.16ms
       { expected_response:true }...: avg=120.92ms min=5.69ms  med=118.59ms max=323.5ms  p(90)=157.89ms p(95)=170.26ms p(99.9)=221.16ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49519
     http_req_receiving.............: avg=88.64µs  min=30.39µs med=82.91µs  max=120.13ms p(90)=113.48µs p(95)=125.98µs p(99.9)=665.74µs
     http_req_sending...............: avg=22.91µs  min=5.38µs  med=16.74µs  max=120.37ms p(90)=22.21µs  p(95)=24.13µs  p(99.9)=584.08µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=120.81ms min=5.59ms  med=118.49ms max=323.18ms p(90)=157.75ms p(95)=170.17ms p(99.9)=220.63ms
     http_reqs......................: 49519   410.186884/s
     iteration_duration.............: avg=121.43ms min=19.64ms med=118.91ms max=337.56ms p(90)=158.22ms p(95)=170.6ms  p(99.9)=223.39ms
     iterations.....................: 49419   409.358542/s
     success_rate...................: 100.00% ✓ 49419      ✗ 0    
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

     checks.........................: 100.00% ✓ 95916      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=6.7µs    min=1.11µs  med=3.36µs   max=4.19ms   p(90)=4.75µs   p(95)=5.34µs   p(99.9)=1.4ms   
     http_req_connecting............: avg=3.15µs   min=0s      med=0s       max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=1.38ms  
     http_req_duration..............: avg=186.91ms min=5.91ms  med=169.8ms  max=813.49ms p(90)=212.56ms p(95)=243.42ms p(99.9)=713.1ms 
       { expected_response:true }...: avg=186.91ms min=5.91ms  med=169.8ms  max=813.49ms p(90)=212.56ms p(95)=243.42ms p(99.9)=713.1ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 32072
     http_req_receiving.............: avg=112.73µs min=31.04µs med=91.13µs  max=117.22ms p(90)=121.13µs p(95)=133.02µs p(99.9)=715.11µs
     http_req_sending...............: avg=29.66µs  min=5.15µs  med=17.1µs   max=91.82ms  p(90)=21.35µs  p(95)=23.16µs  p(99.9)=494.94µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.77ms min=5.76ms  med=169.69ms max=813.37ms p(90)=212.32ms p(95)=243.18ms p(99.9)=712.67ms
     http_reqs......................: 32072   265.056064/s
     iteration_duration.............: avg=187.76ms min=39.21ms med=170.17ms max=813.75ms p(90)=212.92ms p(95)=244.01ms p(99.9)=713.44ms
     iterations.....................: 31972   264.229623/s
     success_rate...................: 100.00% ✓ 31972      ✗ 0    
     vus............................: 10      min=10       max=50 
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

     checks.........................: 100.00% ✓ 95256      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   316 kB/s
     http_req_blocked...............: avg=7.41µs   min=1.48µs  med=3.55µs   max=4.18ms   p(90)=4.96µs   p(95)=5.55µs   p(99.9)=1.8ms   
     http_req_connecting............: avg=3.61µs   min=0s      med=0s       max=4.15ms   p(90)=0s       p(95)=0s       p(99.9)=1.78ms  
     http_req_duration..............: avg=188.17ms min=7.68ms  med=193.47ms max=391.86ms p(90)=202.77ms p(95)=208.35ms p(99.9)=279.78ms
       { expected_response:true }...: avg=188.17ms min=7.68ms  med=193.47ms max=391.86ms p(90)=202.77ms p(95)=208.35ms p(99.9)=279.78ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31852
     http_req_receiving.............: avg=92.37µs  min=35.84µs med=85.96µs  max=100.29ms p(90)=115.95µs p(95)=126.53µs p(99.9)=502.28µs
     http_req_sending...............: avg=30.81µs  min=6.43µs  med=17.11µs  max=117.66ms p(90)=21.88µs  p(95)=23.67µs  p(99.9)=530.54µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=188.05ms min=7.59ms  med=193.35ms max=391.38ms p(90)=202.65ms p(95)=208.22ms p(99.9)=277.27ms
     http_reqs......................: 31852   263.286458/s
     iteration_duration.............: avg=189.06ms min=28.98ms med=193.75ms max=407.16ms p(90)=203.06ms p(95)=208.7ms  p(99.9)=288.14ms
     iterations.....................: 31752   262.459865/s
     success_rate...................: 100.00% ✓ 31752      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

