## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-fed-net-11 | 16.7.0-p.39 | 3,649 | 4,026 | 3,580 | 3.8% |  |
| fusion-nightly-net-10 | 16.7.0-p.39 | 3,593 | 3,911 | 3,529 | 3.5% |  |
| fusion-nightly-net-11 | 16.7.0-p.39 | 3,589 | 3,927 | 3,574 | 3.4% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.39 | 3,578 | 3,943 | 3,497 | 3.8% |  |
| fusion-nightly-aot-11 | 16.7.0-p.39 | 3,518 | 3,803 | 3,506 | 2.9% |  |
| fusion-nightly-fed-aot-11 | 16.7.0-p.39 | 3,496 | 3,782 | 3,423 | 3.1% |  |
| feddi-gateway | 3c75a7db8876 | 3,288 | 3,503 | 3,261 | 2.5% |  |
| hive-router | v0.3.5 | 2,514 | 2,727 | 2,473 | 3.5% |  |
| fusion-net-11 | 16.6.9 | 2,469 | 2,598 | 2,446 | 2.1% |  |
| fusion-net-10 | 16.6.9 | 2,468 | 2,582 | 2,452 | 1.8% |  |
| fusion-fed-net-10 | 16.6.9 | 2,391 | 2,481 | 2,375 | 1.5% |  |
| fusion-fed-net-11 | 16.6.9 | 2,375 | 2,468 | 2,365 | 1.5% |  |
| fusion-aot-11 | 16.6.9 | 2,142 | 2,225 | 2,132 | 1.5% |  |
| fusion-fed-aot-11 | 16.6.9 | 1,962 | 2,041 | 1,943 | 1.7% |  |
| grafbase | 0.53.5 | 1,637 | 1,703 | 1,632 | 1.5% |  |
| cosmo | 0.361.0 | 1,388 | 1,438 | 1,367 | 1.6% |  |
| caliban | 3.2.0 | 1,349 | 1,415 | 1,339 | 2.0% |  |
| hive-gateway-router-runtime | 2.15.2 | 512 | 526 | 508 | 1.3% |  |
| apollo-router | v2.18.0 | 414 | 434 | 411 | 2.2% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 406 | 425 | 404 | 1.9% |  |
| apollo-gateway | 2.14.4 | 267 | 271 | 265 | 0.7% |  |
| hive-gateway | 2.15.2 | 265 | 272 | 263 | 1.1% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1315227     ✗ 0     
     data_received..................: 38 GB   320 MB/s
     data_sent......................: 527 MB  4.4 MB/s
     http_req_blocked...............: avg=2.63µs   min=802ns   med=1.88µs  max=27.21ms  p(90)=3.14µs   p(95)=3.81µs  p(99.9)=28.06µs
     http_req_connecting............: avg=166ns    min=0s      med=0s      max=2.99ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.46ms  min=1.19ms  med=12.16ms max=285.54ms p(90)=21.16ms  p(95)=25.34ms p(99.9)=50.31ms
       { expected_response:true }...: avg=13.46ms  min=1.19ms  med=12.16ms max=285.54ms p(90)=21.16ms  p(95)=25.34ms p(99.9)=50.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 438509
     http_req_receiving.............: avg=542.66µs min=50.66µs med=78.27µs max=169.75ms p(90)=865.11µs p(95)=2.71ms  p(99.9)=28.01ms
     http_req_sending...............: avg=60.7µs   min=4.28µs  med=7.84µs  max=162.77ms p(90)=14.16µs  p(95)=89.74µs p(99.9)=9.95ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=12.86ms  min=1.11ms  med=11.57ms max=285.09ms p(90)=20.38ms  p(95)=24.3ms  p(99.9)=47.63ms
     http_reqs......................: 438509  3649.670644/s
     iteration_duration.............: avg=13.67ms  min=1.6ms   med=12.36ms max=305.54ms p(90)=21.39ms  p(95)=25.61ms p(99.9)=50.88ms
     iterations.....................: 438409  3648.838353/s
     success_rate...................: 100.00% ✓ 438409      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1294971     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 519 MB  4.3 MB/s
     http_req_blocked...............: avg=3.91µs   min=952ns    med=2.23µs  max=33.2ms   p(90)=3.55µs  p(95)=4.23µs  p(99.9)=33.08µs
     http_req_connecting............: avg=924ns    min=0s       med=0s      max=32.38ms  p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.67ms  min=912.8µs  med=12.39ms max=287.23ms p(90)=21.71ms p(95)=25.98ms p(99.9)=51.9ms 
       { expected_response:true }...: avg=13.67ms  min=912.8µs  med=12.39ms max=287.23ms p(90)=21.71ms p(95)=25.98ms p(99.9)=51.9ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 431757
     http_req_receiving.............: avg=805.09µs min=52.16µs  med=80.79µs max=182.69ms p(90)=2.07ms  p(95)=4.53ms  p(99.9)=30.94ms
     http_req_sending...............: avg=62.41µs  min=4.31µs   med=8.18µs  max=129.12ms p(90)=14.78µs p(95)=95.34µs p(99.9)=10.46ms
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=12.8ms   min=843.54µs med=11.51ms max=224.94ms p(90)=20.57ms p(95)=24.53ms p(99.9)=48.5ms 
     http_reqs......................: 431757  3593.619647/s
     iteration_duration.............: avg=13.89ms  min=1.43ms   med=12.59ms max=295.06ms p(90)=21.95ms p(95)=26.26ms p(99.9)=52.72ms
     iterations.....................: 431657  3592.787322/s
     success_rate...................: 100.00% ✓ 431657      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1293339     ✗ 0     
     data_received..................: 38 GB   315 MB/s
     data_sent......................: 518 MB  4.3 MB/s
     http_req_blocked...............: avg=2.78µs   min=821ns    med=1.96µs  max=26.52ms  p(90)=3.29µs  p(95)=4.05µs  p(99.9)=31.32µs
     http_req_connecting............: avg=210ns    min=0s       med=0s      max=3.58ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.69ms  min=914.72µs med=12.48ms max=279.39ms p(90)=21.25ms p(95)=25.23ms p(99.9)=51.06ms
       { expected_response:true }...: avg=13.69ms  min=914.72µs med=12.48ms max=279.39ms p(90)=21.25ms p(95)=25.23ms p(99.9)=51.06ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 431213
     http_req_receiving.............: avg=787.47µs min=51.93µs  med=81.57µs max=274.41ms p(90)=2.27ms  p(95)=4.42ms  p(99.9)=27.35ms
     http_req_sending...............: avg=59.79µs  min=4.52µs   med=8.13µs  max=192.02ms p(90)=14.98µs p(95)=93.42µs p(99.9)=9.42ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=12.84ms  min=834.87µs med=11.61ms max=228.34ms p(90)=20.09ms p(95)=23.87ms p(99.9)=47.64ms
     http_reqs......................: 431213  3589.567061/s
     iteration_duration.............: avg=13.9ms   min=1.38ms   med=12.68ms max=300.1ms  p(90)=21.48ms p(95)=25.49ms p(99.9)=52.47ms
     iterations.....................: 431113  3588.734626/s
     success_rate...................: 100.00% ✓ 431113      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1289673     ✗ 0     
     data_received..................: 38 GB   314 MB/s
     data_sent......................: 517 MB  4.3 MB/s
     http_req_blocked...............: avg=5.6µs    min=831ns   med=1.97µs  max=112.91ms p(90)=3.23µs  p(95)=3.91µs  p(99.9)=28.82µs
     http_req_connecting............: avg=2.81µs   min=0s      med=0s      max=112.72ms p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.72ms  min=1.24ms  med=12.51ms max=278.57ms p(90)=21.31ms p(95)=25.47ms p(99.9)=51.96ms
       { expected_response:true }...: avg=13.72ms  min=1.24ms  med=12.51ms max=278.57ms p(90)=21.31ms p(95)=25.47ms p(99.9)=51.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 429991
     http_req_receiving.............: avg=729.04µs min=51.98µs med=82.13µs max=137.61ms p(90)=1.95ms  p(95)=3.8ms   p(99.9)=28.45ms
     http_req_sending...............: avg=62.6µs   min=4.57µs  med=8.18µs  max=126.17ms p(90)=14.7µs  p(95)=93.05µs p(99.9)=10.79ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=12.93ms  min=1.16ms  med=11.71ms max=269.53ms p(90)=20.32ms p(95)=24.26ms p(99.9)=48.98ms
     http_reqs......................: 429991  3578.272456/s
     iteration_duration.............: avg=13.94ms  min=1.64ms  med=12.71ms max=299.07ms p(90)=21.53ms p(95)=25.73ms p(99.9)=52.67ms
     iterations.....................: 429891  3577.440282/s
     success_rate...................: 100.00% ✓ 429891      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1267980     ✗ 0     
     data_received..................: 37 GB   309 MB/s
     data_sent......................: 508 MB  4.2 MB/s
     http_req_blocked...............: avg=2.88µs   min=852ns    med=1.94µs  max=31.15ms  p(90)=3.22µs  p(95)=3.93µs  p(99.9)=26.34µs
     http_req_connecting............: avg=226ns    min=0s       med=0s      max=3.81ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=13.97ms  min=995.81µs med=12.84ms max=266.57ms p(90)=21.19ms p(95)=24.97ms p(99.9)=50.22ms
       { expected_response:true }...: avg=13.97ms  min=995.81µs med=12.84ms max=266.57ms p(90)=21.19ms p(95)=24.97ms p(99.9)=50.22ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 422760
     http_req_receiving.............: avg=939.37µs min=49.72µs  med=83.2µs  max=192.37ms p(90)=2.91ms  p(95)=5.01ms  p(99.9)=30.1ms 
     http_req_sending...............: avg=58.54µs  min=4.62µs   med=8.08µs  max=148.9ms  p(90)=15.25µs p(95)=93.58µs p(99.9)=9.08ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=12.97ms  min=900.01µs med=11.83ms max=266.3ms  p(90)=19.88ms p(95)=23.41ms p(99.9)=47.26ms
     http_reqs......................: 422760  3518.727889/s
     iteration_duration.............: avg=14.18ms  min=1.54ms   med=13.04ms max=278.62ms p(90)=21.41ms p(95)=25.22ms p(99.9)=51.34ms
     iterations.....................: 422660  3517.895566/s
     success_rate...................: 100.00% ✓ 422660      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1260024     ✗ 0     
     data_received..................: 37 GB   307 MB/s
     data_sent......................: 505 MB  4.2 MB/s
     http_req_blocked...............: avg=3.27µs   min=811ns   med=2.19µs  max=26.27ms  p(90)=3.64µs  p(95)=4.32µs  p(99.9)=32.17µs
     http_req_connecting............: avg=209ns    min=0s      med=0s      max=3.49ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=14.05ms  min=1.31ms  med=12.9ms  max=292.91ms p(90)=21.12ms p(95)=25.3ms  p(99.9)=50.12ms
       { expected_response:true }...: avg=14.05ms  min=1.31ms  med=12.9ms  max=292.91ms p(90)=21.12ms p(95)=25.3ms  p(99.9)=50.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 420108
     http_req_receiving.............: avg=828.26µs min=50.78µs med=83.75µs max=101.73ms p(90)=2.35ms  p(95)=4.15ms  p(99.9)=29.08ms
     http_req_sending...............: avg=59.4µs   min=4.31µs  med=8.39µs  max=197.81ms p(90)=15.4µs  p(95)=96.77µs p(99.9)=8.94ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=13.16ms  min=1.18ms  med=11.98ms max=292.27ms p(90)=20.03ms p(95)=23.84ms p(99.9)=47.17ms
     http_reqs......................: 420108  3496.111865/s
     iteration_duration.............: avg=14.27ms  min=1.81ms  med=13.1ms  max=302.91ms p(90)=21.34ms p(95)=25.59ms p(99.9)=51.19ms
     iterations.....................: 420008  3495.279671/s
     success_rate...................: 100.00% ✓ 420008      ✗ 0     
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

     checks.........................: 100.00% ✓ 1184778     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 475 MB  4.0 MB/s
     http_req_blocked...............: avg=3.27µs  min=811ns    med=2.26µs  max=27.08ms  p(90)=3.85µs  p(95)=4.69µs   p(99.9)=37.44µs
     http_req_connecting............: avg=262ns   min=0s       med=0s      max=4.3ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.96ms min=986.05µs med=14.22ms max=296.59ms p(90)=21.32ms p(95)=25.3ms   p(99.9)=47.15ms
       { expected_response:true }...: avg=14.96ms min=986.05µs med=14.22ms max=296.59ms p(90)=21.32ms p(95)=25.3ms   p(99.9)=47.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 395026
     http_req_receiving.............: avg=110.9µs min=25.33µs  med=48.68µs max=130.8ms  p(90)=97.99µs p(95)=214.18µs p(99.9)=9.72ms 
     http_req_sending...............: avg=56.87µs min=4.85µs   med=9.37µs  max=148.25ms p(90)=17.15µs p(95)=111.88µs p(99.9)=8.39ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.79ms min=922.14µs med=14.09ms max=265.82ms p(90)=21.08ms p(95)=24.88ms  p(99.9)=45.72ms
     http_reqs......................: 395026  3288.127942/s
     iteration_duration.............: avg=15.18ms min=1.55ms   med=14.42ms max=316.45ms p(90)=21.54ms p(95)=25.56ms  p(99.9)=48.5ms 
     iterations.....................: 394926  3287.29556/s
     success_rate...................: 100.00% ✓ 394926      ✗ 0     
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

     checks.........................: 100.00% ✓ 906471      ✗ 0     
     data_received..................: 26 GB   220 MB/s
     data_sent......................: 363 MB  3.0 MB/s
     http_req_blocked...............: avg=2.89µs  min=811ns   med=2.14µs  max=12.43ms  p(90)=3.69µs  p(95)=4.49µs   p(99.9)=38.46µs
     http_req_connecting............: avg=289ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.63ms min=1.79ms  med=19.45ms max=303.46ms p(90)=26.83ms p(95)=29.13ms  p(99.9)=47.76ms
       { expected_response:true }...: avg=19.63ms min=1.79ms  med=19.45ms max=303.46ms p(90)=26.83ms p(95)=29.13ms  p(99.9)=47.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 302257
     http_req_receiving.............: avg=88.72µs min=27.06µs med=51.59µs max=177.41ms p(90)=91.99µs p(95)=128.82µs p(99.9)=6.18ms 
     http_req_sending...............: avg=41.36µs min=4.61µs  med=9.27µs  max=44.01ms  p(90)=16.97µs p(95)=73.06µs  p(99.9)=3.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.5ms  min=1.68ms  med=19.33ms max=302.99ms p(90)=26.68ms p(95)=28.94ms  p(99.9)=46.89ms
     http_reqs......................: 302257  2514.059139/s
     iteration_duration.............: avg=19.84ms min=3.18ms  med=19.64ms max=311.42ms p(90)=27.03ms p(95)=29.34ms  p(99.9)=48.37ms
     iterations.....................: 302157  2513.227377/s
     success_rate...................: 100.00% ✓ 302157      ✗ 0     
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

     checks.........................: 100.00% ✓ 890256      ✗ 0     
     data_received..................: 26 GB   217 MB/s
     data_sent......................: 357 MB  3.0 MB/s
     http_req_blocked...............: avg=3.55µs  min=941ns   med=2.51µs  max=16.45ms  p(90)=4.19µs  p(95)=5.03µs   p(99.9)=33.1µs 
     http_req_connecting............: avg=400ns   min=0s      med=0s      max=4.2ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=19.98ms min=1.58ms  med=19.3ms  max=291.87ms p(90)=26.93ms p(95)=30.14ms  p(99.9)=52.75ms
       { expected_response:true }...: avg=19.98ms min=1.58ms  med=19.3ms  max=291.87ms p(90)=26.93ms p(95)=30.14ms  p(99.9)=52.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 296852
     http_req_receiving.............: avg=2.18ms  min=52.84µs med=1.81ms  max=265.77ms p(90)=4.55ms  p(95)=6.12ms   p(99.9)=29.77ms
     http_req_sending...............: avg=52.79µs min=4.84µs  med=9.27µs  max=255.53ms p(90)=19.41µs p(95)=101.48µs p(99.9)=6.71ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.74ms min=1.49ms  med=16.99ms max=275.43ms p(90)=24.12ms p(95)=27.18ms  p(99.9)=47.91ms
     http_reqs......................: 296852  2469.512982/s
     iteration_duration.............: avg=20.2ms  min=2.53ms  med=19.51ms max=308.65ms p(90)=27.15ms p(95)=30.38ms  p(99.9)=53.45ms
     iterations.....................: 296752  2468.681082/s
     success_rate...................: 100.00% ✓ 296752      ✗ 0     
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

     checks.........................: 100.00% ✓ 889716      ✗ 0     
     data_received..................: 26 GB   216 MB/s
     data_sent......................: 357 MB  3.0 MB/s
     http_req_blocked...............: avg=2.67µs  min=852ns   med=1.97µs max=3.57ms   p(90)=3.28µs  p(95)=4µs     p(99.9)=25.6µs 
     http_req_connecting............: avg=334ns   min=0s      med=0s     max=3.53ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20ms    min=1.54ms  med=19.4ms max=297.72ms p(90)=27.08ms p(95)=29.99ms p(99.9)=50.51ms
       { expected_response:true }...: avg=20ms    min=1.54ms  med=19.4ms max=297.72ms p(90)=27.08ms p(95)=29.99ms p(99.9)=50.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 296672
     http_req_receiving.............: avg=1.51ms  min=50.68µs med=1.12ms max=159.17ms p(90)=3.33ms  p(95)=4.37ms  p(99.9)=25.49ms
     http_req_sending...............: avg=44.35µs min=4.56µs  med=8.16µs max=159.29ms p(90)=16.87µs p(95)=84.59µs p(99.9)=4.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s     max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=18.44ms min=1.46ms  med=17.8ms max=293.25ms p(90)=25.31ms p(95)=28.23ms p(99.9)=47.07ms
     http_reqs......................: 296672  2468.07944/s
     iteration_duration.............: avg=20.22ms min=2.91ms  med=19.6ms max=328.28ms p(90)=27.29ms p(95)=30.22ms p(99.9)=51.09ms
     iterations.....................: 296572  2467.247519/s
     success_rate...................: 100.00% ✓ 296572      ✗ 0     
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

     checks.........................: 100.00% ✓ 862179      ✗ 0     
     data_received..................: 25 GB   210 MB/s
     data_sent......................: 346 MB  2.9 MB/s
     http_req_blocked...............: avg=3.29µs  min=912ns   med=2.17µs  max=21.26ms  p(90)=3.98µs  p(95)=4.82µs  p(99.9)=32.3µs 
     http_req_connecting............: avg=460ns   min=0s      med=0s      max=4.28ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.64ms min=1.77ms  med=20.02ms max=269.27ms p(90)=28.03ms p(95)=31.01ms p(99.9)=52.13ms
       { expected_response:true }...: avg=20.64ms min=1.77ms  med=20.02ms max=269.27ms p(90)=28.03ms p(95)=31.01ms p(99.9)=52.13ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 287493
     http_req_receiving.............: avg=1.49ms  min=51.38µs med=1.06ms  max=47.7ms   p(90)=3.37ms  p(95)=4.45ms  p(99.9)=25.29ms
     http_req_sending...............: avg=46.66µs min=4.85µs  med=8.74µs  max=178.33ms p(90)=19.47µs p(95)=94.19µs p(99.9)=4.67ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.09ms min=1.69ms  med=18.44ms max=268.91ms p(90)=26.28ms p(95)=29.23ms p(99.9)=49.27ms
     http_reqs......................: 287493  2391.267196/s
     iteration_duration.............: avg=20.86ms min=2.94ms  med=20.23ms max=297.32ms p(90)=28.25ms p(95)=31.25ms p(99.9)=52.83ms
     iterations.....................: 287393  2390.43543/s
     success_rate...................: 100.00% ✓ 287393      ✗ 0     
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

     checks.........................: 100.00% ✓ 856464      ✗ 0     
     data_received..................: 25 GB   208 MB/s
     data_sent......................: 343 MB  2.9 MB/s
     http_req_blocked...............: avg=3.29µs  min=872ns  med=2.14µs  max=21.57ms  p(90)=3.93µs  p(95)=4.87µs  p(99.9)=30.26µs
     http_req_connecting............: avg=567ns   min=0s     med=0s      max=7.56ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.77ms min=1.8ms  med=20.11ms max=281.73ms p(90)=27.49ms p(95)=30.57ms p(99.9)=54.64ms
       { expected_response:true }...: avg=20.77ms min=1.8ms  med=20.11ms max=281.73ms p(90)=27.49ms p(95)=30.57ms p(99.9)=54.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 285588
     http_req_receiving.............: avg=2.22ms  min=52.5µs med=1.93ms  max=211.64ms p(90)=4.5ms   p(95)=6.05ms  p(99.9)=30.36ms
     http_req_sending...............: avg=51.97µs min=4.76µs med=8.89µs  max=167.47ms p(90)=20.74µs p(95)=96.46µs p(99.9)=6.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=18.5ms  min=1.71ms med=17.77ms max=261.01ms p(90)=24.61ms p(95)=27.56ms p(99.9)=49.81ms
     http_reqs......................: 285588  2375.564695/s
     iteration_duration.............: avg=21ms    min=2.71ms med=20.32ms max=290.7ms  p(90)=27.71ms p(95)=30.8ms  p(99.9)=55.29ms
     iterations.....................: 285488  2374.732879/s
     success_rate...................: 100.00% ✓ 285488      ✗ 0     
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

     checks.........................: 100.00% ✓ 772278      ✗ 0     
     data_received..................: 23 GB   188 MB/s
     data_sent......................: 309 MB  2.6 MB/s
     http_req_blocked...............: avg=3.58µs  min=992ns   med=2.62µs  max=12.67ms  p(90)=4.38µs  p(95)=5.19µs  p(99.9)=38.17µs
     http_req_connecting............: avg=383ns   min=0s      med=0s      max=4.01ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=23.06ms min=1.67ms  med=22.48ms max=298.92ms p(90)=29.86ms p(95)=32.84ms p(99.9)=56.83ms
       { expected_response:true }...: avg=23.06ms min=1.67ms  med=22.48ms max=298.92ms p(90)=29.86ms p(95)=32.84ms p(99.9)=56.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 257526
     http_req_receiving.............: avg=2.75ms  min=53.39µs med=2.67ms  max=175.25ms p(90)=4.9ms   p(95)=6.12ms  p(99.9)=28.79ms
     http_req_sending...............: avg=48.45µs min=4.86µs  med=9.39µs  max=148.22ms p(90)=19.53µs p(95)=96.87µs p(99.9)=5.32ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=20.25ms min=1.59ms  med=19.57ms max=298.34ms p(90)=26.67ms p(95)=29.52ms p(99.9)=50.42ms
     http_reqs......................: 257526  2142.076641/s
     iteration_duration.............: avg=23.29ms min=2.91ms  med=22.69ms max=308.82ms p(90)=30.08ms p(95)=33.08ms p(99.9)=57.35ms
     iterations.....................: 257426  2141.24485/s
     success_rate...................: 100.00% ✓ 257426      ✗ 0     
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

     checks.........................: 100.00% ✓ 707694      ✗ 0     
     data_received..................: 21 GB   172 MB/s
     data_sent......................: 284 MB  2.4 MB/s
     http_req_blocked...............: avg=3.18µs  min=912ns   med=2.2µs   max=12.89ms  p(90)=4.11µs  p(95)=4.94µs  p(99.9)=27.36µs
     http_req_connecting............: avg=409ns   min=0s      med=0s      max=3.59ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.19ms min=1.96ms  med=24.61ms max=256.66ms p(90)=31.53ms p(95)=34.27ms p(99.9)=55.12ms
       { expected_response:true }...: avg=25.19ms min=1.96ms  med=24.61ms max=256.66ms p(90)=31.53ms p(95)=34.27ms p(99.9)=55.12ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 235998
     http_req_receiving.............: avg=3ms     min=53.36µs med=2.97ms  max=238.5ms  p(90)=4.99ms  p(95)=6.08ms  p(99.9)=27.63ms
     http_req_sending...............: avg=41.33µs min=4.86µs  med=9.13µs  max=114.85ms p(90)=21.27µs p(95)=87.43µs p(99.9)=3.57ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=22.14ms min=1.82ms  med=21.52ms max=220.63ms p(90)=28.17ms p(95)=30.74ms p(99.9)=49.5ms 
     http_reqs......................: 235998  1962.475123/s
     iteration_duration.............: avg=25.42ms min=4.39ms  med=24.82ms max=326.26ms p(90)=31.75ms p(95)=34.5ms  p(99.9)=55.81ms
     iterations.....................: 235898  1961.643559/s
     success_rate...................: 100.00% ✓ 235898      ✗ 0     
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

     checks.........................: 100.00% ✓ 590580      ✗ 0     
     data_received..................: 17 GB   144 MB/s
     data_sent......................: 237 MB  2.0 MB/s
     http_req_blocked...............: avg=3.75µs  min=891ns   med=2.22µs  max=7.9ms    p(90)=4.3µs    p(95)=5.43µs   p(99.9)=39.04µs
     http_req_connecting............: avg=931ns   min=0s      med=0s      max=7.87ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=30.22ms min=2.23ms  med=29.99ms max=290.48ms p(90)=39.29ms  p(95)=42.29ms  p(99.9)=63.96ms
       { expected_response:true }...: avg=30.22ms min=2.23ms  med=29.99ms max=290.48ms p(90)=39.29ms  p(95)=42.29ms  p(99.9)=63.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 196960
     http_req_receiving.............: avg=92.36µs min=27.51µs med=54.82µs max=77.93ms  p(90)=124.79µs p(95)=206.62µs p(99.9)=3.57ms 
     http_req_sending...............: avg=40.03µs min=4.61µs  med=9.28µs  max=49.53ms  p(90)=22.46µs  p(95)=106.45µs p(99.9)=2.93ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=30.09ms min=2.09ms  med=29.87ms max=288.02ms p(90)=39.15ms  p(95)=42.12ms  p(99.9)=63.38ms
     http_reqs......................: 196960  1637.553942/s
     iteration_duration.............: avg=30.46ms min=7.2ms   med=30.2ms  max=310.54ms p(90)=39.5ms   p(95)=42.51ms  p(99.9)=64.56ms
     iterations.....................: 196860  1636.722527/s
     success_rate...................: 100.00% ✓ 196860      ✗ 0     
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

     checks.........................: 100.00% ✓ 500730      ✗ 0     
     data_received..................: 15 GB   121 MB/s
     data_sent......................: 201 MB  1.7 MB/s
     http_req_blocked...............: avg=3.82µs  min=1.08µs med=2.81µs  max=4.42ms   p(90)=4.46µs   p(95)=5.22µs   p(99.9)=37.36µs
     http_req_connecting............: avg=645ns   min=0s     med=0s      max=4.38ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=35.7ms  min=2.44ms med=34.76ms max=296.67ms p(90)=51.33ms  p(95)=56.51ms  p(99.9)=82.16ms
       { expected_response:true }...: avg=35.7ms  min=2.44ms med=34.76ms max=296.67ms p(90)=51.33ms  p(95)=56.51ms  p(99.9)=82.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 167010
     http_req_receiving.............: avg=83.03µs min=25.9µs med=64.09µs max=138.52ms p(90)=105.73µs p(95)=126.68µs p(99.9)=1.25ms 
     http_req_sending...............: avg=27.29µs min=4.82µs med=11.63µs max=138.85ms p(90)=18.51µs  p(95)=23.26µs  p(99.9)=1.2ms  
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.59ms min=2.32ms med=34.66ms max=295.5ms  p(90)=51.22ms  p(95)=56.4ms   p(99.9)=81.99ms
     http_reqs......................: 167010  1388.1285/s
     iteration_duration.............: avg=35.94ms min=4.16ms med=34.97ms max=313ms    p(90)=51.54ms  p(95)=56.73ms  p(99.9)=82.58ms
     iterations.....................: 166910  1387.297335/s
     success_rate...................: 100.00% ✓ 166910      ✗ 0     
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

     checks.........................: 100.00% ✓ 486669      ✗ 0     
     data_received..................: 14 GB   118 MB/s
     data_sent......................: 195 MB  1.6 MB/s
     http_req_blocked...............: avg=3.36µs  min=932ns   med=2.46µs  max=3.53ms   p(90)=4.29µs   p(95)=5.05µs   p(99.9)=33.39µs
     http_req_connecting............: avg=546ns   min=0s      med=0s      max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=36.73ms min=2.57ms  med=35.65ms max=298ms    p(90)=52.09ms  p(95)=57.61ms  p(99.9)=87.23ms
       { expected_response:true }...: avg=36.73ms min=2.57ms  med=35.65ms max=298ms    p(90)=52.09ms  p(95)=57.61ms  p(99.9)=87.23ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 162323
     http_req_receiving.............: avg=80.17µs min=27.91µs med=62.3µs  max=148.49ms p(90)=100.76µs p(95)=118.67µs p(99.9)=1.28ms 
     http_req_sending...............: avg=26.53µs min=4.76µs  med=11.65µs max=196.7ms  p(90)=18.81µs  p(95)=22.58µs  p(99.9)=1.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=36.62ms min=2.42ms  med=35.56ms max=285.37ms p(90)=51.98ms  p(95)=57.5ms   p(99.9)=86.88ms
     http_reqs......................: 162323  1349.135339/s
     iteration_duration.............: avg=36.97ms min=5.42ms  med=35.88ms max=311.59ms p(90)=52.3ms   p(95)=57.84ms  p(99.9)=87.9ms 
     iterations.....................: 162223  1348.304196/s
     success_rate...................: 100.00% ✓ 162223      ✗ 0     
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

     checks.........................: 100.00% ✓ 185259     ✗ 0    
     data_received..................: 5.4 GB  45 MB/s
     data_sent......................: 74 MB   616 kB/s
     http_req_blocked...............: avg=7.79µs  min=1.07µs  med=2.74µs  max=9.26ms   p(90)=4.3µs    p(95)=4.93µs   p(99.9)=49.38µs 
     http_req_connecting............: avg=4.52µs  min=0s      med=0s      max=9.22ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=96.76ms min=4.42ms  med=93.71ms max=335.05ms p(90)=116.58ms p(95)=127.48ms p(99.9)=222.99ms
       { expected_response:true }...: avg=96.76ms min=4.42ms  med=93.71ms max=335.05ms p(90)=116.58ms p(95)=127.48ms p(99.9)=222.99ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61853
     http_req_receiving.............: avg=79.34µs min=28.01µs med=72.76µs max=17.69ms  p(90)=107.3µs  p(95)=119.81µs p(99.9)=602.18µs
     http_req_sending...............: avg=25.15µs min=4.78µs  med=13.63µs max=141.9ms  p(90)=19.7µs   p(95)=21.84µs  p(99.9)=671.89µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=96.66ms min=4.34ms  med=93.62ms max=334.61ms p(90)=116.49ms p(95)=127.38ms p(99.9)=222.87ms
     http_reqs......................: 61853   512.902012/s
     iteration_duration.............: avg=97.17ms min=34.09ms med=93.96ms max=353.61ms p(90)=116.84ms p(95)=127.77ms p(99.9)=224.53ms
     iterations.....................: 61753   512.072784/s
     success_rate...................: 100.00% ✓ 61753      ✗ 0    
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

     checks.........................: 100.00% ✓ 149787     ✗ 0    
     data_received..................: 4.4 GB  36 MB/s
     data_sent......................: 60 MB   498 kB/s
     http_req_blocked...............: avg=5.74µs   min=1.39µs  med=3.64µs   max=3.63ms   p(90)=5.19µs   p(95)=5.8µs    p(99.9)=131.76µs
     http_req_connecting............: avg=1.84µs   min=0s      med=0s       max=3.59ms   p(90)=0s       p(95)=0s       p(99.9)=49.54µs 
     http_req_duration..............: avg=119.68ms min=5.21ms  med=117.42ms max=322.06ms p(90)=158.66ms p(95)=170.46ms p(99.9)=219.02ms
       { expected_response:true }...: avg=119.68ms min=5.21ms  med=117.42ms max=322.06ms p(90)=158.66ms p(95)=170.46ms p(99.9)=219.02ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 50029
     http_req_receiving.............: avg=87.53µs  min=31.51µs med=82.53µs  max=46.14ms  p(90)=113.18µs p(95)=124.99µs p(99.9)=499.53µs
     http_req_sending...............: avg=30.64µs  min=6.07µs  med=16.85µs  max=135.2ms  p(90)=22.14µs  p(95)=24.12µs  p(99.9)=591.19µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=119.57ms min=5.03ms  med=117.31ms max=299.53ms p(90)=158.53ms p(95)=170.34ms p(99.9)=218.05ms
     http_reqs......................: 50029   414.615799/s
     iteration_duration.............: avg=120.19ms min=22.36ms med=117.75ms max=329.95ms p(90)=158.96ms p(95)=170.76ms p(99.9)=221.14ms
     iterations.....................: 49929   413.787048/s
     success_rate...................: 100.00% ✓ 49929      ✗ 0    
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

     checks.........................: 100.00% ✓ 146982     ✗ 0    
     data_received..................: 4.3 GB  36 MB/s
     data_sent......................: 59 MB   488 kB/s
     http_req_blocked...............: avg=6.03µs   min=1.3µs   med=3.71µs   max=4.33ms   p(90)=5.31µs   p(95)=5.95µs   p(99.9)=406.32µs
     http_req_connecting............: avg=2.03µs   min=0s      med=0s       max=4.29ms   p(90)=0s       p(95)=0s       p(99.9)=332.33µs
     http_req_duration..............: avg=121.96ms min=5.8ms   med=119.48ms max=342.4ms  p(90)=159.51ms p(95)=171.58ms p(99.9)=222.29ms
       { expected_response:true }...: avg=121.96ms min=5.8ms   med=119.48ms max=342.4ms  p(90)=159.51ms p(95)=171.58ms p(99.9)=222.29ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49094
     http_req_receiving.............: avg=90.59µs  min=31.09µs med=83.4µs   max=126.39ms p(90)=114.13µs p(95)=126.18µs p(99.9)=638.12µs
     http_req_sending...............: avg=24.4µs   min=5.63µs  med=17.8µs   max=112.37ms p(90)=22.85µs  p(95)=24.76µs  p(99.9)=574.85µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.85ms min=5.72ms  med=119.38ms max=335.29ms p(90)=159.4ms  p(95)=171.46ms p(99.9)=221.63ms
     http_reqs......................: 49094   406.659419/s
     iteration_duration.............: avg=122.49ms min=34.81ms med=119.82ms max=352.34ms p(90)=159.83ms p(95)=171.92ms p(99.9)=224.56ms
     iterations.....................: 48994   405.831091/s
     success_rate...................: 100.00% ✓ 48994      ✗ 0    
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

     checks.........................: 100.00% ✓ 96921      ✗ 0    
     data_received..................: 2.8 GB  24 MB/s
     data_sent......................: 39 MB   322 kB/s
     http_req_blocked...............: avg=6.74µs   min=1.43µs  med=3.46µs   max=3.97ms   p(90)=4.92µs   p(95)=5.52µs   p(99.9)=1.39ms  
     http_req_connecting............: avg=2.97µs   min=0s      med=0s       max=3.93ms   p(90)=0s       p(95)=0s       p(99.9)=1.37ms  
     http_req_duration..............: avg=184.93ms min=7.81ms  med=184.86ms max=392.97ms p(90)=197.91ms p(95)=202.74ms p(99.9)=272.33ms
       { expected_response:true }...: avg=184.93ms min=7.81ms  med=184.86ms max=392.97ms p(90)=197.91ms p(95)=202.74ms p(99.9)=272.33ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32407
     http_req_receiving.............: avg=104.35µs min=33.74µs med=90.5µs   max=110.03ms p(90)=121.75µs p(95)=134.79µs p(99.9)=631.07µs
     http_req_sending...............: avg=28.96µs  min=5.75µs  med=17.83µs  max=94.56ms  p(90)=22.64µs  p(95)=24.57µs  p(99.9)=501.53µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.8ms  min=7.64ms  med=184.74ms max=392.79ms p(90)=197.78ms p(95)=202.6ms  p(99.9)=270.73ms
     http_reqs......................: 32407   267.925469/s
     iteration_duration.............: avg=185.79ms min=42.22ms med=185.23ms max=422.28ms p(90)=198.19ms p(95)=203.05ms p(99.9)=273.92ms
     iterations.....................: 32307   267.098717/s
     success_rate...................: 100.00% ✓ 32307      ✗ 0    
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

     checks.........................: 100.00% ✓ 96228      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=6.26µs   min=1.09µs  med=3.21µs   max=4.22ms   p(90)=4.57µs   p(95)=5.15µs   p(99.9)=1.25ms  
     http_req_connecting............: avg=2.85µs   min=0s      med=0s       max=4.18ms   p(90)=0s       p(95)=0s       p(99.9)=1.23ms  
     http_req_duration..............: avg=186.42ms min=5.92ms  med=168.5ms  max=850.9ms  p(90)=213.58ms p(95)=242.16ms p(99.9)=736.83ms
       { expected_response:true }...: avg=186.42ms min=5.92ms  med=168.5ms  max=850.9ms  p(90)=213.58ms p(95)=242.16ms p(99.9)=736.83ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32176
     http_req_receiving.............: avg=95.3µs   min=29.08µs med=89.94µs  max=94.71ms  p(90)=120.55µs p(95)=132.84µs p(99.9)=614.73µs
     http_req_sending...............: avg=32.76µs  min=5.47µs  med=17.25µs  max=149.57ms p(90)=21.63µs  p(95)=23.4µs   p(99.9)=588.9µs 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.29ms min=5.79ms  med=168.38ms max=850.79ms p(90)=213.47ms p(95)=241.97ms p(99.9)=736.72ms
     http_reqs......................: 32176   265.620105/s
     iteration_duration.............: avg=187.27ms min=36.63ms med=168.85ms max=851.2ms  p(90)=214ms    p(95)=242.64ms p(99.9)=737.08ms
     iterations.....................: 32076   264.794582/s
     success_rate...................: 100.00% ✓ 32076      ✗ 0    
     vus............................: 25      min=25       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

