## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net11 | 16.7.0-p.36 | 3,605 | 3,936 | 3,577 | 3.3% |  |
| fusion-nightly | 16.7.0-p.36 | 3,527 | 3,801 | 3,485 | 3.0% |  |
| fusion-nightly-fed | 16.7.0-p.36 | 3,485 | 3,838 | 3,440 | 3.8% |  |
| feddi-gateway | 3c75a7db8876 | 3,101 | 3,303 | 3,058 | 2.6% |  |
| fusion | 16.6.9 | 2,548 | 2,652 | 2,532 | 1.6% |  |
| hive-router | v0.3.5 | 2,523 | 2,697 | 2,489 | 2.8% |  |
| grafbase | 0.53.5 | 1,649 | 1,700 | 1,643 | 1.1% |  |
| cosmo | 0.359.0 | 1,435 | 1,486 | 1,430 | 1.5% |  |
| caliban | 3.2.0 | 1,341 | 1,406 | 1,329 | 1.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 505 | 525 | 503 | 1.4% |  |
| apollo-router | v2.18.0 | 446 | 464 | 434 | 1.9% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 387 | 412 | 380 | 2.8% |  |
| apollo-gateway | 2.14.4 | 264 | 271 | 263 | 0.9% |  |
| hive-gateway | 2.15.2 | 246 | 253 | 243 | 1.5% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net11 (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1299261     ✗ 0     
     data_received..................: 38 GB   316 MB/s
     data_sent......................: 521 MB  4.3 MB/s
     http_req_blocked...............: avg=2.64µs   min=801ns    med=1.95µs  max=21.69ms  p(90)=3.26µs  p(95)=4.02µs  p(99.9)=28.49µs
     http_req_connecting............: avg=173ns    min=0s       med=0s      max=3.25ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.62ms  min=1.08ms   med=12.46ms max=295.08ms p(90)=20.88ms p(95)=24.68ms p(99.9)=51.28ms
       { expected_response:true }...: avg=13.62ms  min=1.08ms   med=12.46ms max=295.08ms p(90)=20.88ms p(95)=24.68ms p(99.9)=51.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 433187
     http_req_receiving.............: avg=699.71µs min=50.39µs  med=81.14µs max=165.55ms p(90)=1.94ms  p(95)=3.67ms  p(99.9)=26.59ms
     http_req_sending...............: avg=58.72µs  min=4.36µs   med=8.07µs  max=153.97ms p(90)=15.15µs p(95)=95.1µs  p(99.9)=9.08ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=12.87ms  min=955.73µs med=11.67ms max=271ms    p(90)=19.97ms p(95)=23.55ms p(99.9)=47.9ms 
     http_reqs......................: 433187  3605.414736/s
     iteration_duration.............: avg=13.84ms  min=1.65ms   med=12.66ms max=304.47ms p(90)=21.1ms  p(95)=24.94ms p(99.9)=52.12ms
     iterations.....................: 433087  3604.582436/s
     success_rate...................: 100.00% ✓ 433087      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1271073     ✗ 0     
     data_received..................: 37 GB   309 MB/s
     data_sent......................: 509 MB  4.2 MB/s
     http_req_blocked...............: avg=3.21µs   min=821ns   med=2.01µs  max=21.82ms  p(90)=3.31µs  p(95)=3.98µs  p(99.9)=28.23µs
     http_req_connecting............: avg=575ns    min=0s      med=0s      max=9.19ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.93ms  min=1.16ms  med=12.84ms max=307.41ms p(90)=21.13ms p(95)=24.95ms p(99.9)=49.22ms
       { expected_response:true }...: avg=13.93ms  min=1.16ms  med=12.84ms max=307.41ms p(90)=21.13ms p(95)=24.95ms p(99.9)=49.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 423791
     http_req_receiving.............: avg=852.02µs min=51.15µs med=83.1µs  max=243.77ms p(90)=2.46ms  p(95)=4.42ms  p(99.9)=28.74ms
     http_req_sending...............: avg=58.23µs  min=4.46µs  med=8.2µs   max=236.52ms p(90)=15.06µs p(95)=94.28µs p(99.9)=8.88ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.02ms  min=1.02ms  med=11.91ms max=301.29ms p(90)=19.94ms p(95)=23.61ms p(99.9)=46.9ms 
     http_reqs......................: 423791  3527.09927/s
     iteration_duration.............: avg=14.15ms  min=1.64ms  med=13.04ms max=329.71ms p(90)=21.35ms p(95)=25.21ms p(99.9)=49.97ms
     iterations.....................: 423691  3526.266997/s
     success_rate...................: 100.00% ✓ 423691      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed (HotChocolate subgraphs) (16.7.0-p.36)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1256400     ✗ 0     
     data_received..................: 37 GB   306 MB/s
     data_sent......................: 503 MB  4.2 MB/s
     http_req_blocked...............: avg=6.08µs   min=931ns  med=2.47µs  max=60.64ms  p(90)=3.84µs  p(95)=4.54µs   p(99.9)=35.26µs
     http_req_connecting............: avg=3.04µs   min=0s     med=0s      max=60.61ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.09ms  min=1.3ms  med=12.84ms max=235.62ms p(90)=22.1ms  p(95)=26.37ms  p(99.9)=53.29ms
       { expected_response:true }...: avg=14.09ms  min=1.3ms  med=12.84ms max=235.62ms p(90)=22.1ms  p(95)=26.37ms  p(99.9)=53.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 418900
     http_req_receiving.............: avg=725.87µs min=53.4µs med=84.57µs max=57.39ms  p(90)=1.86ms  p(95)=3.92ms   p(99.9)=27.48ms
     http_req_sending...............: avg=65.01µs  min=4.78µs med=9.1µs   max=54.75ms  p(90)=16.29µs p(95)=101.69µs p(99.9)=11.08ms
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=13.29ms  min=1.17ms med=12.04ms max=227.53ms p(90)=21.09ms p(95)=25.16ms  p(99.9)=50.9ms 
     http_reqs......................: 418900  3485.158686/s
     iteration_duration.............: avg=14.31ms  min=1.72ms med=13.05ms max=295.57ms p(90)=22.34ms p(95)=26.66ms  p(99.9)=54.21ms
     iterations.....................: 418800  3484.326707/s
     success_rate...................: 100.00% ✓ 418800      ✗ 0     
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

     checks.........................: 100.00% ✓ 1117362     ✗ 0     
     data_received..................: 33 GB   271 MB/s
     data_sent......................: 448 MB  3.7 MB/s
     http_req_blocked...............: avg=3.23µs  min=842ns    med=2.07µs  max=16.51ms  p(90)=3.48µs  p(95)=4.23µs   p(99.9)=32.35µs
     http_req_connecting............: avg=649ns   min=0s       med=0s      max=9.43ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=15.89ms min=998.72µs med=15.45ms max=277.13ms p(90)=23.19ms p(95)=26.46ms  p(99.9)=47.13ms
       { expected_response:true }...: avg=15.89ms min=998.72µs med=15.45ms max=277.13ms p(90)=23.19ms p(95)=26.46ms  p(99.9)=47.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 372554
     http_req_receiving.............: avg=96.87µs min=25.86µs  med=48.05µs max=186.4ms  p(90)=92.34µs p(95)=192.26µs p(99.9)=7.56ms 
     http_req_sending...............: avg=54.4µs  min=4.58µs   med=8.75µs  max=163.36ms p(90)=15.61µs p(95)=104.89µs p(99.9)=10.14ms
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=15.74ms min=926.8µs  med=15.33ms max=255.15ms p(90)=23.01ms p(95)=26.17ms  p(99.9)=45.96ms
     http_reqs......................: 372554  3101.137862/s
     iteration_duration.............: avg=16.1ms  min=1.58ms   med=15.64ms max=301.93ms p(90)=23.39ms p(95)=26.69ms  p(99.9)=48ms   
     iterations.....................: 372454  3100.305462/s
     success_rate...................: 100.00% ✓ 372454      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion (HotChocolate subgraphs) (16.6.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 918780      ✗ 0     
     data_received..................: 27 GB   223 MB/s
     data_sent......................: 368 MB  3.1 MB/s
     http_req_blocked...............: avg=2.93µs  min=851ns   med=2µs     max=15.42ms  p(90)=3.61µs  p(95)=4.42µs  p(99.9)=27.24µs
     http_req_connecting............: avg=320ns   min=0s      med=0s      max=4.1ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.36ms min=1.54ms  med=18.74ms max=314.43ms p(90)=26.27ms p(95)=29.29ms p(99.9)=50.34ms
       { expected_response:true }...: avg=19.36ms min=1.54ms  med=18.74ms max=314.43ms p(90)=26.27ms p(95)=29.29ms p(99.9)=50.34ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 306360
     http_req_receiving.............: avg=1.44ms  min=50.78µs med=1.01ms  max=156.03ms p(90)=3.26ms  p(95)=4.29ms  p(99.9)=24.83ms
     http_req_sending...............: avg=46.12µs min=4.42µs  med=8.27µs  max=159.41ms p(90)=18.29µs p(95)=92.86µs p(99.9)=5.28ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.87ms min=1.45ms  med=17.22ms max=307.89ms p(90)=24.56ms p(95)=27.55ms p(99.9)=47.26ms
     http_reqs......................: 306360  2548.623829/s
     iteration_duration.............: avg=19.58ms min=2.67ms  med=18.94ms max=352.2ms  p(90)=26.48ms p(95)=29.52ms p(99.9)=51.12ms
     iterations.....................: 306260  2547.791924/s
     success_rate...................: 100.00% ✓ 306260      ✗ 0     
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

     checks.........................: 100.00% ✓ 909828      ✗ 0     
     data_received..................: 27 GB   221 MB/s
     data_sent......................: 365 MB  3.0 MB/s
     http_req_blocked...............: avg=3.39µs  min=1.02µs  med=2.76µs  max=12.71ms  p(90)=4.43µs  p(95)=5.25µs   p(99.9)=38.91µs
     http_req_connecting............: avg=198ns   min=0s      med=0s      max=2.83ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.55ms min=1.66ms  med=19.29ms max=283.5ms  p(90)=26.92ms p(95)=29.58ms  p(99.9)=50.06ms
       { expected_response:true }...: avg=19.55ms min=1.66ms  med=19.29ms max=283.5ms  p(90)=26.92ms p(95)=29.58ms  p(99.9)=50.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 303376
     http_req_receiving.............: avg=99.76µs min=25.71µs med=52.74µs max=124.31ms p(90)=96.22µs p(95)=156.41µs p(99.9)=8.49ms 
     http_req_sending...............: avg=47.72µs min=4.68µs  med=10.69µs max=115.75ms p(90)=18.82µs p(95)=104.45µs p(99.9)=4.13ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.4ms  min=1.55ms  med=19.17ms max=282.93ms p(90)=26.76ms p(95)=29.34ms  p(99.9)=49.14ms
     http_reqs......................: 303376  2523.667131/s
     iteration_duration.............: avg=19.77ms min=3.51ms  med=19.5ms  max=294ms    p(90)=27.14ms p(95)=29.81ms  p(99.9)=50.49ms
     iterations.....................: 303276  2522.83527/s
     success_rate...................: 100.00% ✓ 303276      ✗ 0     
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

     checks.........................: 100.00% ✓ 595194      ✗ 0     
     data_received..................: 17 GB   145 MB/s
     data_sent......................: 239 MB  2.0 MB/s
     http_req_blocked...............: avg=4.19µs   min=1.06µs  med=2.91µs  max=15.56ms  p(90)=5.28µs   p(95)=6.39µs   p(99.9)=48.19µs
     http_req_connecting............: avg=496ns    min=0s      med=0s      max=4.29ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=29.97ms  min=2.32ms  med=29.88ms max=320.29ms p(90)=39.39ms  p(95)=42.54ms  p(99.9)=67.44ms
       { expected_response:true }...: avg=29.97ms  min=2.32ms  med=29.88ms max=320.29ms p(90)=39.39ms  p(95)=42.54ms  p(99.9)=67.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 198498
     http_req_receiving.............: avg=130.42µs min=28.62µs med=58.92µs max=259.13ms p(90)=133.63µs p(95)=234.66µs p(99.9)=5.58ms 
     http_req_sending...............: avg=44.51µs  min=4.69µs  med=10.64µs max=27.83ms  p(90)=24.98µs  p(95)=124.17µs p(99.9)=3.57ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=29.79ms  min=2.24ms  med=29.75ms max=108.75ms p(90)=39.24ms  p(95)=42.34ms  p(99.9)=66.39ms
     http_reqs......................: 198498  1649.836559/s
     iteration_duration.............: avg=30.23ms  min=3.55ms  med=30.12ms max=340.74ms p(90)=39.63ms  p(95)=42.77ms  p(99.9)=67.86ms
     iterations.....................: 198398  1649.005399/s
     success_rate...................: 100.00% ✓ 198398      ✗ 0     
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

     checks.........................: 100.00% ✓ 517839      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=4.25µs  min=1.01µs med=2.27µs  max=8.93ms   p(90)=3.95µs  p(95)=4.71µs   p(99.9)=31.21µs
     http_req_connecting............: avg=1.55µs  min=0s     med=0s      max=8.89ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.52ms min=2.32ms med=33.57ms max=280.58ms p(90)=49.53ms p(95)=54.64ms  p(99.9)=78.03ms
       { expected_response:true }...: avg=34.52ms min=2.32ms med=33.57ms max=280.58ms p(90)=49.53ms p(95)=54.64ms  p(99.9)=78.03ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 172713
     http_req_receiving.............: avg=74.76µs min=25.8µs med=58.81µs max=100.95ms p(90)=98.29µs p(95)=116.58µs p(99.9)=1.13ms 
     http_req_sending...............: avg=26.92µs min=4.7µs  med=10.32µs max=204.01ms p(90)=17.44µs p(95)=22.07µs  p(99.9)=1.21ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.42ms min=2.21ms med=33.48ms max=279.29ms p(90)=49.43ms p(95)=54.53ms  p(99.9)=77.8ms 
     http_reqs......................: 172713  1435.632311/s
     iteration_duration.............: avg=34.75ms min=5.18ms med=33.78ms max=296.79ms p(90)=49.73ms p(95)=54.84ms  p(99.9)=78.56ms
     iterations.....................: 172613  1434.801087/s
     success_rate...................: 100.00% ✓ 172613      ✗ 0     
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

     checks.........................: 100.00% ✓ 484029      ✗ 0     
     data_received..................: 14 GB   117 MB/s
     data_sent......................: 194 MB  1.6 MB/s
     http_req_blocked...............: avg=3.48µs  min=932ns   med=2.52µs  max=3.8ms    p(90)=4.28µs   p(95)=5.02µs   p(99.9)=34.05µs
     http_req_connecting............: avg=623ns   min=0s      med=0s      max=3.75ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.94ms min=2.56ms  med=35.9ms  max=305.35ms p(90)=52.47ms  p(95)=57.95ms  p(99.9)=87.14ms
       { expected_response:true }...: avg=36.94ms min=2.56ms  med=35.9ms  max=305.35ms p(90)=52.47ms  p(95)=57.95ms  p(99.9)=87.14ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 161443
     http_req_receiving.............: avg=79.37µs min=28.63µs med=62.68µs max=109.75ms p(90)=101.68µs p(95)=119.22µs p(99.9)=1.38ms 
     http_req_sending...............: avg=24.43µs min=4.82µs  med=11.16µs max=50.17ms  p(90)=18.97µs  p(95)=22.91µs  p(99.9)=1.13ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.83ms min=2.49ms  med=35.8ms  max=298.03ms p(90)=52.36ms  p(95)=57.83ms  p(99.9)=86.74ms
     http_reqs......................: 161443  1341.681809/s
     iteration_duration.............: avg=37.18ms min=5.79ms  med=36.12ms max=321.17ms p(90)=52.7ms   p(95)=58.17ms  p(99.9)=87.67ms
     iterations.....................: 161343  1340.850753/s
     success_rate...................: 100.00% ✓ 161343      ✗ 0     
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

     checks.........................: 100.00% ✓ 182409     ✗ 0    
     data_received..................: 5.3 GB  44 MB/s
     data_sent......................: 73 MB   607 kB/s
     http_req_blocked...............: avg=5.09µs  min=1.17µs  med=3.29µs  max=4.08ms   p(90)=4.82µs   p(95)=5.47µs   p(99.9)=61.55µs 
     http_req_connecting............: avg=1.55µs  min=0s      med=0s      max=4.04ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=98.29ms min=4.23ms  med=95.38ms max=327.34ms p(90)=118.65ms p(95)=129.76ms p(99.9)=231.64ms
       { expected_response:true }...: avg=98.29ms min=4.23ms  med=95.38ms max=327.34ms p(90)=118.65ms p(95)=129.76ms p(99.9)=231.64ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 60903
     http_req_receiving.............: avg=90.14µs min=30.51µs med=77.93µs max=110.29ms p(90)=112.28µs p(95)=125.5µs  p(99.9)=670.43µs
     http_req_sending...............: avg=29.11µs min=5.65µs  med=14.91µs max=182.19ms p(90)=20.75µs  p(95)=22.89µs  p(99.9)=609.67µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=98.17ms min=4.16ms  med=95.28ms max=326.63ms p(90)=118.52ms p(95)=129.6ms  p(99.9)=231.28ms
     http_reqs......................: 60903   505.137/s
     iteration_duration.............: avg=98.7ms  min=35.73ms med=95.64ms max=345.67ms p(90)=118.96ms p(95)=130.05ms p(99.9)=232.9ms 
     iterations.....................: 60803   504.307588/s
     success_rate...................: 100.00% ✓ 60803      ✗ 0    
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

     checks.........................: 100.00% ✓ 161175     ✗ 0    
     data_received..................: 4.7 GB  39 MB/s
     data_sent......................: 65 MB   536 kB/s
     http_req_blocked...............: avg=5.2µs    min=1.11µs  med=3.19µs   max=4.14ms   p(90)=4.67µs   p(95)=5.23µs   p(99.9)=63.68µs 
     http_req_connecting............: avg=1.83µs   min=0s      med=0s       max=4.1ms    p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=111.22ms min=5.26ms  med=109.15ms max=318.77ms p(90)=147.01ms p(95)=158.03ms p(99.9)=203.23ms
       { expected_response:true }...: avg=111.22ms min=5.26ms  med=109.15ms max=318.77ms p(90)=147.01ms p(95)=158.03ms p(99.9)=203.23ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 53825
     http_req_receiving.............: avg=88.9µs   min=26.67µs med=80.39µs  max=138.7ms  p(90)=110.38µs p(95)=122.5µs  p(99.9)=504.59µs
     http_req_sending...............: avg=22.69µs  min=5µs     med=16.64µs  max=97.02ms  p(90)=21.55µs  p(95)=23.33µs  p(99.9)=554.38µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=111.11ms min=5.14ms  med=109.05ms max=317.85ms p(90)=146.91ms p(95)=157.93ms p(99.9)=202.71ms
     http_reqs......................: 53825   446.145774/s
     iteration_duration.............: avg=111.7ms  min=14.91ms med=109.48ms max=341.19ms p(90)=147.31ms p(95)=158.31ms p(99.9)=206.11ms
     iterations.....................: 53725   445.316892/s
     success_rate...................: 100.00% ✓ 53725      ✗ 0    
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

     checks.........................: 100.00% ✓ 139860     ✗ 0    
     data_received..................: 4.1 GB  34 MB/s
     data_sent......................: 56 MB   465 kB/s
     http_req_blocked...............: avg=5.27µs   min=1.09µs  med=3.03µs   max=3.88ms   p(90)=4.4µs    p(95)=4.95µs   p(99.9)=851.73µs
     http_req_connecting............: avg=2.03µs   min=0s      med=0s       max=3.84ms   p(90)=0s       p(95)=0s       p(99.9)=829.34µs
     http_req_duration..............: avg=128.21ms min=5.64ms  med=125.68ms max=330.94ms p(90)=167.42ms p(95)=180.52ms p(99.9)=232.9ms 
       { expected_response:true }...: avg=128.21ms min=5.64ms  med=125.68ms max=330.94ms p(90)=167.42ms p(95)=180.52ms p(99.9)=232.9ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 46720
     http_req_receiving.............: avg=82.22µs  min=30.73µs med=78.35µs  max=54.01ms  p(90)=107.67µs p(95)=119.84µs p(99.9)=590.72µs
     http_req_sending...............: avg=21.05µs  min=5.34µs  med=15.76µs  max=27.13ms  p(90)=20.82µs  p(95)=22.58µs  p(99.9)=501.71µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=128.11ms min=5.52ms  med=125.58ms max=327.31ms p(90)=167.32ms p(95)=180.4ms  p(99.9)=232.78ms
     http_reqs......................: 46720   387.021304/s
     iteration_duration.............: avg=128.74ms min=15.44ms med=125.98ms max=340.04ms p(90)=167.76ms p(95)=180.82ms p(99.9)=234.38ms
     iterations.....................: 46620   386.192919/s
     success_rate...................: 100.00% ✓ 46620      ✗ 0    
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

     checks.........................: 100.00% ✓ 95784      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=6.59µs   min=1.14µs  med=3.09µs   max=3.74ms   p(90)=4.4µs    p(95)=4.91µs   p(99.9)=1.7ms   
     http_req_connecting............: avg=3.3µs    min=0s      med=0s       max=3.7ms    p(90)=0s       p(95)=0s       p(99.9)=1.68ms  
     http_req_duration..............: avg=187.17ms min=7.98ms  med=185.96ms max=361.3ms  p(90)=197.55ms p(95)=202.49ms p(99.9)=271.19ms
       { expected_response:true }...: avg=187.17ms min=7.98ms  med=185.96ms max=361.3ms  p(90)=197.55ms p(95)=202.49ms p(99.9)=271.19ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32028
     http_req_receiving.............: avg=89.58µs  min=30.75µs med=87.32µs  max=8.45ms   p(90)=116.51µs p(95)=127.37µs p(99.9)=465.53µs
     http_req_sending...............: avg=25.66µs  min=5.15µs  med=16.43µs  max=66.27ms  p(90)=20.7µs   p(95)=22.45µs  p(99.9)=525.36µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=187.05ms min=7.87ms  med=185.85ms max=361.12ms p(90)=197.44ms p(95)=202.37ms p(99.9)=271.06ms
     http_reqs......................: 32028   264.696667/s
     iteration_duration.............: avg=188.01ms min=40.94ms med=186.32ms max=371.74ms p(90)=197.85ms p(95)=202.77ms p(99.9)=271.96ms
     iterations.....................: 31928   263.870213/s
     success_rate...................: 100.00% ✓ 31928      ✗ 0    
     vus............................: 10      min=10       max=50 
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

     checks.........................: 100.00% ✓ 89319      ✗ 0    
     data_received..................: 2.6 GB  22 MB/s
     data_sent......................: 36 MB   296 kB/s
     http_req_blocked...............: avg=13.04µs  min=1.38µs  med=3.55µs   max=9.6ms    p(90)=4.94µs   p(95)=5.56µs   p(99.9)=4.99ms  
     http_req_connecting............: avg=9.09µs   min=0s      med=0s       max=9.55ms   p(90)=0s       p(95)=0s       p(99.9)=4.94ms  
     http_req_duration..............: avg=200.7ms  min=6.39ms  med=182.11ms max=681.8ms  p(90)=236.28ms p(95)=317.42ms p(99.9)=617.36ms
       { expected_response:true }...: avg=200.7ms  min=6.39ms  med=182.11ms max=681.8ms  p(90)=236.28ms p(95)=317.42ms p(99.9)=617.36ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 29873
     http_req_receiving.............: avg=94.85µs  min=36.17µs med=87.47µs  max=84.04ms  p(90)=117.62µs p(95)=128.56µs p(99.9)=696.07µs
     http_req_sending...............: avg=29.39µs  min=6.23µs  med=17.25µs  max=69.55ms  p(90)=21.8µs   p(95)=23.59µs  p(99.9)=541.45µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=200.58ms min=6.26ms  med=182.01ms max=681.72ms p(90)=236.16ms p(95)=317.32ms p(99.9)=617.24ms
     http_reqs......................: 29873   246.63518/s
     iteration_duration.............: avg=201.64ms min=45.36ms med=182.51ms max=682.1ms  p(90)=236.94ms p(95)=323.78ms p(99.9)=617.63ms
     iterations.....................: 29773   245.809568/s
     success_rate...................: 100.00% ✓ 29773      ✗ 0    
     vus............................: 16      min=16       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

