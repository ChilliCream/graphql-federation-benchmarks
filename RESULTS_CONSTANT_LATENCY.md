## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 3,424 | 3,434 | 3,422 | 0.2% | 388 MB | 115.9 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,411 | 3,420 | 3,398 | 0.3% | 387 MB | 116.2 KB |  |
| fusion-aot-11 | 16.7.3 | 3,358 | 3,378 | 3,351 | 0.3% | 133 MB | 40.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,350 | 3,361 | 3,343 | 0.2% | 131 MB | 40.0 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,278 | 3,306 | 3,237 | 0.8% | 2,303 MB | 719.4 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,772 | 2,785 | 2,764 | 0.3% | 410 MB | 151.4 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,766 | 2,775 | 2,760 | 0.2% | 416 MB | 154.1 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,747 | 2,753 | 2,744 | 0.1% | 131 MB | 48.8 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,746 | 2,756 | 2,732 | 0.3% | 154 MB | 57.4 KB |  |
| hive-router | v0.3.6 | 2,035 | 2,047 | 2,021 | 0.5% | 92 MB | 46.2 KB |  |
| grafbase | 0.53.5 | 1,442 | 1,460 | 1,436 | 0.6% | 101 MB | 71.4 KB |  |
| cosmo | 0.363.0 | 1,425 | 1,427 | 1,423 | 0.1% | 148 MB | 106.5 KB |  |
| caliban | 3.2.0 | 1,363 | 1,364 | 1,361 | 0.1% | 4,567 MB | 3,430.9 KB |  |
| apollo-router | v2.19.0 | 530 | 531 | 529 | 0.1% | 180 MB | 347.8 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 520 | 520 | 518 | 0.2% | 2,746 MB | 5,408.2 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 418 | 419 | 418 | 0.1% | 206 MB | 503.9 KB |  |
| apollo-gateway | 2.14.4 | 266 | 266 | 265 | 0.2% | 2,177 MB | 8,378.8 KB |  |
| hive-gateway | 2.15.3 | 265 | 266 | 264 | 0.3% | 3,642 MB | 14,072.0 KB |  |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1242234     ✗ 0     
     data_received..................: 36 GB   300 MB/s
     data_sent......................: 498 MB  4.1 MB/s
     http_req_blocked...............: avg=2.39µs  min=781ns   med=1.77µs  max=4.13ms   p(90)=3.04µs  p(95)=3.89µs   p(99.9)=22.18µs
     http_req_connecting............: avg=222ns   min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.28ms min=8.1ms   med=13.87ms max=276.57ms p(90)=17.73ms p(95)=19.08ms  p(99.9)=26.76ms
       { expected_response:true }...: avg=14.28ms min=8.1ms   med=13.87ms max=276.57ms p(90)=17.73ms p(95)=19.08ms  p(99.9)=26.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 414178
     http_req_receiving.............: avg=70.19µs min=24.48µs med=43.62µs max=193.4ms  p(90)=92.32µs p(95)=165.42µs p(99.9)=1.98ms 
     http_req_sending...............: avg=30.43µs min=4.03µs  med=7.66µs  max=160.15ms p(90)=16.21µs p(95)=88.49µs  p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.18ms min=8.02ms  med=13.77ms max=271.98ms p(90)=17.63ms p(95)=18.96ms  p(99.9)=26.5ms 
     http_reqs......................: 414178  3424.430255/s
     iteration_duration.............: avg=14.48ms min=8.23ms  med=14.06ms max=291.94ms p(90)=17.92ms p(95)=19.27ms  p(99.9)=27.01ms
     iterations.....................: 414078  3423.603453/s
     success_rate...................: 100.00% ✓ 414078      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1237620     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 496 MB  4.1 MB/s
     http_req_blocked...............: avg=2.42µs  min=791ns   med=1.8µs   max=4.97ms   p(90)=3.04µs  p(95)=3.84µs   p(99.9)=24.04µs
     http_req_connecting............: avg=224ns   min=0s      med=0s      max=3.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.34ms min=8.24ms  med=13.94ms max=268.91ms p(90)=17.79ms p(95)=19.12ms  p(99.9)=26.85ms
       { expected_response:true }...: avg=14.34ms min=8.24ms  med=13.94ms max=268.91ms p(90)=17.79ms p(95)=19.12ms  p(99.9)=26.85ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 412640
     http_req_receiving.............: avg=67.56µs min=23.69µs med=41.82µs max=44.21ms  p(90)=90.91µs p(95)=170.45µs p(99.9)=1.98ms 
     http_req_sending...............: avg=30.65µs min=4.1µs   med=7.62µs  max=214.97ms p(90)=16.56µs p(95)=90.75µs  p(99.9)=1.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.24ms min=8.19ms  med=13.84ms max=268.37ms p(90)=17.68ms p(95)=19.01ms  p(99.9)=26.63ms
     http_reqs......................: 412640  3411.665394/s
     iteration_duration.............: avg=14.53ms min=8.39ms  med=14.13ms max=293.28ms p(90)=17.98ms p(95)=19.31ms  p(99.9)=27.07ms
     iterations.....................: 412540  3410.838604/s
     success_rate...................: 100.00% ✓ 412540      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1218519     ✗ 0     
     data_received..................: 36 GB   294 MB/s
     data_sent......................: 488 MB  4.0 MB/s
     http_req_blocked...............: avg=2.75µs  min=922ns   med=2.28µs  max=3.25ms   p(90)=3.6µs   p(95)=4.32µs   p(99.9)=32.07µs
     http_req_connecting............: avg=115ns   min=0s      med=0s      max=2.12ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.56ms min=8.34ms  med=14.09ms max=285.01ms p(90)=18.11ms p(95)=19.57ms  p(99.9)=28.15ms
       { expected_response:true }...: avg=14.56ms min=8.34ms  med=14.09ms max=285.01ms p(90)=18.11ms p(95)=19.57ms  p(99.9)=28.15ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 406273
     http_req_receiving.............: avg=72.39µs min=24.58µs med=45.15µs max=45.51ms  p(90)=94.5µs  p(95)=187.16µs p(99.9)=1.98ms 
     http_req_sending...............: avg=33.46µs min=4.54µs  med=8.58µs  max=202.03ms p(90)=16.91µs p(95)=100.05µs p(99.9)=1.99ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.45ms min=8.27ms  med=13.99ms max=284.63ms p(90)=17.99ms p(95)=19.44ms  p(99.9)=27.87ms
     http_reqs......................: 406273  3358.372066/s
     iteration_duration.............: avg=14.76ms min=8.51ms  med=14.29ms max=294.56ms p(90)=18.3ms  p(95)=19.76ms  p(99.9)=28.38ms
     iterations.....................: 406173  3357.545436/s
     success_rate...................: 100.00% ✓ 406173      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1215657     ✗ 0     
     data_received..................: 36 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.38µs  min=751ns   med=1.87µs  max=3.84ms   p(90)=3.12µs  p(95)=3.85µs   p(99.9)=28.04µs
     http_req_connecting............: avg=148ns   min=0s      med=0s      max=2.72ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.6ms  min=8.31ms  med=14.17ms max=262.36ms p(90)=18.08ms p(95)=19.47ms  p(99.9)=27.64ms
       { expected_response:true }...: avg=14.6ms  min=8.31ms  med=14.17ms max=262.36ms p(90)=18.08ms p(95)=19.47ms  p(99.9)=27.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405319
     http_req_receiving.............: avg=72.7µs  min=24.45µs med=43.71µs max=193.81ms p(90)=91.4µs  p(95)=169.59µs p(99.9)=1.73ms 
     http_req_sending...............: avg=30.93µs min=4.2µs   med=7.82µs  max=154.81ms p(90)=15.95µs p(95)=91.57µs  p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.49ms min=8.27ms  med=14.07ms max=261.54ms p(90)=17.98ms p(95)=19.36ms  p(99.9)=27.27ms
     http_reqs......................: 405319  3350.689682/s
     iteration_duration.............: avg=14.79ms min=8.49ms  med=14.36ms max=286.86ms p(90)=18.27ms p(95)=19.66ms  p(99.9)=27.86ms
     iterations.....................: 405219  3349.863002/s
     success_rate...................: 100.00% ✓ 405219      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-10-25-0247)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1189533     ✗ 0     
     data_received..................: 35 GB   287 MB/s
     data_sent......................: 477 MB  3.9 MB/s
     http_req_blocked...............: avg=3.02µs  min=901ns   med=2.41µs  max=6.51ms   p(90)=3.88µs  p(95)=4.67µs   p(99.9)=30.48µs
     http_req_connecting............: avg=242ns   min=0s      med=0s      max=3.6ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.92ms min=8.38ms  med=14.54ms max=274.39ms p(90)=18.07ms p(95)=19.36ms  p(99.9)=26.98ms
       { expected_response:true }...: avg=14.92ms min=8.38ms  med=14.54ms max=274.39ms p(90)=18.07ms p(95)=19.36ms  p(99.9)=26.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 396611
     http_req_receiving.............: avg=72.5µs  min=23.77µs med=47.28µs max=11.99ms  p(90)=95.32µs p(95)=181.75µs p(99.9)=1.73ms 
     http_req_sending...............: avg=33.48µs min=4.42µs  med=8.92µs  max=163.63ms p(90)=17.55µs p(95)=101.01µs p(99.9)=1.66ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.81ms min=8.27ms  med=14.43ms max=274.07ms p(90)=17.96ms p(95)=19.24ms  p(99.9)=26.74ms
     http_reqs......................: 396611  3278.964143/s
     iteration_duration.............: avg=15.12ms min=8.55ms  med=14.73ms max=293.56ms p(90)=18.26ms p(95)=19.56ms  p(99.9)=27.21ms
     iterations.....................: 396511  3278.137398/s
     success_rate...................: 100.00% ✓ 396511      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1009560     ✗ 0     
     data_received..................: 30 GB   243 MB/s
     data_sent......................: 405 MB  3.3 MB/s
     http_req_blocked...............: avg=2.49µs  min=841ns   med=1.86µs  max=3.39ms   p(90)=3.27µs  p(95)=4.15µs   p(99.9)=25.89µs
     http_req_connecting............: avg=238ns   min=0s      med=0s      max=3.35ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.61ms min=11.83ms med=17.18ms max=282.74ms p(90)=20.76ms p(95)=22.01ms  p(99.9)=28.82ms
       { expected_response:true }...: avg=17.61ms min=11.83ms med=17.18ms max=282.74ms p(90)=20.76ms p(95)=22.01ms  p(99.9)=28.82ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 336620
     http_req_receiving.............: avg=66µs    min=23.78µs med=43.06µs max=153.91ms p(90)=91.31µs p(95)=145.69µs p(99.9)=1.5ms  
     http_req_sending...............: avg=26.89µs min=4.29µs  med=7.87µs  max=24.2ms   p(90)=16.52µs p(95)=82.12µs  p(99.9)=1.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.52ms min=11.77ms med=17.09ms max=282.28ms p(90)=20.66ms p(95)=21.91ms  p(99.9)=28.6ms 
     http_reqs......................: 336620  2772.967869/s
     iteration_duration.............: avg=17.82ms min=11.98ms med=17.38ms max=290.88ms p(90)=20.95ms p(95)=22.21ms  p(99.9)=29.04ms
     iterations.....................: 336520  2772.144101/s
     success_rate...................: 100.00% ✓ 336520      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1007061     ✗ 0     
     data_received..................: 29 GB   242 MB/s
     data_sent......................: 404 MB  3.3 MB/s
     http_req_blocked...............: avg=2.43µs  min=791ns   med=1.79µs  max=4.29ms   p(90)=2.95µs  p(95)=3.65µs   p(99.9)=24.52µs
     http_req_connecting............: avg=295ns   min=0s      med=0s      max=4.23ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.66ms min=11.69ms med=17.22ms max=291.33ms p(90)=20.83ms p(95)=22.12ms  p(99.9)=28.68ms
       { expected_response:true }...: avg=17.66ms min=11.69ms med=17.22ms max=291.33ms p(90)=20.83ms p(95)=22.12ms  p(99.9)=28.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 335787
     http_req_receiving.............: avg=65.89µs min=24.07µs med=44.44µs max=196.06ms p(90)=88.4µs  p(95)=138.01µs p(99.9)=1.38ms 
     http_req_sending...............: avg=25.87µs min=4.22µs  med=7.68µs  max=119.09ms p(90)=15.12µs p(95)=76.63µs  p(99.9)=1.33ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.57ms min=11.6ms  med=17.14ms max=291.22ms p(90)=20.73ms p(95)=22.02ms  p(99.9)=28.44ms
     http_reqs......................: 335787  2766.019007/s
     iteration_duration.............: avg=17.86ms min=11.9ms  med=17.42ms max=302.61ms p(90)=21.02ms p(95)=22.31ms  p(99.9)=28.87ms
     iterations.....................: 335687  2765.195265/s
     success_rate...................: 100.00% ✓ 335687      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1000425     ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=3.52µs  min=912ns   med=2.29µs  max=8.85ms   p(90)=3.8µs   p(95)=4.63µs   p(99.9)=29.66µs
     http_req_connecting............: avg=851ns   min=0s      med=0s      max=8.82ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.77ms min=11.8ms  med=17.33ms max=281.1ms  p(90)=20.84ms p(95)=22.13ms  p(99.9)=29.58ms
       { expected_response:true }...: avg=17.77ms min=11.8ms  med=17.33ms max=281.1ms  p(90)=20.84ms p(95)=22.13ms  p(99.9)=29.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 333575
     http_req_receiving.............: avg=68.37µs min=23.48µs med=45.15µs max=166.47ms p(90)=92.67µs p(95)=154.34µs p(99.9)=1.36ms 
     http_req_sending...............: avg=30.36µs min=4.51µs  med=8.88µs  max=168.06ms p(90)=17.61µs p(95)=90.11µs  p(99.9)=1.45ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.67ms min=11.71ms med=17.24ms max=280.86ms p(90)=20.74ms p(95)=22.01ms  p(99.9)=29.39ms
     http_reqs......................: 333575  2747.752898/s
     iteration_duration.............: avg=17.98ms min=12ms    med=17.53ms max=297.49ms p(90)=21.05ms p(95)=22.33ms  p(99.9)=29.82ms
     iterations.....................: 333475  2746.929169/s
     success_rate...................: 100.00% ✓ 333475      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1000032     ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=2.51µs  min=791ns   med=1.9µs   max=3.36ms   p(90)=3.23µs  p(95)=4.05µs   p(99.9)=22.92µs
     http_req_connecting............: avg=255ns   min=0s      med=0s      max=3.32ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.78ms min=11.9ms  med=17.38ms max=278.08ms p(90)=20.8ms  p(95)=22.03ms  p(99.9)=29.51ms
       { expected_response:true }...: avg=17.78ms min=11.9ms  med=17.38ms max=278.08ms p(90)=20.8ms  p(95)=22.03ms  p(99.9)=29.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 333444
     http_req_receiving.............: avg=66.86µs min=25.03µs med=45.1µs  max=187.72ms p(90)=90.7µs  p(95)=144.64µs p(99.9)=1.38ms 
     http_req_sending...............: avg=26.86µs min=4.27µs  med=7.96µs  max=26.06ms  p(90)=16.11µs p(95)=81.47µs  p(99.9)=1.4ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.69ms min=11.68ms med=17.29ms max=277.68ms p(90)=20.7ms  p(95)=21.92ms  p(99.9)=29.27ms
     http_reqs......................: 333444  2746.220451/s
     iteration_duration.............: avg=17.99ms min=12.04ms med=17.58ms max=324.16ms p(90)=21ms    p(95)=22.22ms  p(99.9)=29.77ms
     iterations.....................: 333344  2745.396859/s
     success_rate...................: 100.00% ✓ 333344      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 743934      ✗ 0     
     data_received..................: 22 GB   178 MB/s
     data_sent......................: 298 MB  2.4 MB/s
     http_req_blocked...............: avg=3.35µs  min=952ns   med=2.64µs  max=3.43ms   p(90)=4.3µs   p(95)=5.06µs   p(99.9)=36.1µs  
     http_req_connecting............: avg=371ns   min=0s      med=0s      max=3.4ms    p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.96ms min=17.18ms med=23.6ms  max=300.68ms p(90)=27.07ms p(95)=28.16ms  p(99.9)=34.14ms 
       { expected_response:true }...: avg=23.96ms min=17.18ms med=23.6ms  max=300.68ms p(90)=27.07ms p(95)=28.16ms  p(99.9)=34.14ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 248078
     http_req_receiving.............: avg=68.32µs min=23.98µs med=51.5µs  max=43.2ms   p(90)=95.26µs p(95)=122.71µs p(99.9)=973.61µs
     http_req_sending...............: avg=28.14µs min=4.58µs  med=10.33µs max=180.48ms p(90)=18.8µs  p(95)=27.84µs  p(99.9)=999.18µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.87ms min=17.13ms med=23.51ms max=299.97ms p(90)=26.97ms p(95)=28.06ms  p(99.9)=33.97ms 
     http_reqs......................: 248078  2035.440452/s
     iteration_duration.............: avg=24.18ms min=17.39ms med=23.81ms max=313.56ms p(90)=27.28ms p(95)=28.37ms  p(99.9)=34.34ms 
     iterations.....................: 247978  2034.619968/s
     success_rate...................: 100.00% ✓ 247978      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 527214      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3.17µs  min=801ns   med=2.1µs   max=4.09ms   p(90)=4.5µs    p(95)=5.43µs   p(99.9)=38.2µs 
     http_req_connecting............: avg=506ns   min=0s      med=0s      max=4.04ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.88ms min=17.63ms med=33.6ms  max=308.36ms p(90)=39.63ms  p(95)=41.32ms  p(99.9)=49.86ms
       { expected_response:true }...: avg=33.88ms min=17.63ms med=33.6ms  max=308.36ms p(90)=39.63ms  p(95)=41.32ms  p(99.9)=49.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 175838
     http_req_receiving.............: avg=77.24µs min=24.96µs med=52.54µs max=81.9ms   p(90)=115.37µs p(95)=157.06µs p(99.9)=1.27ms 
     http_req_sending...............: avg=28.02µs min=4.46µs  med=9.04µs  max=86.13ms  p(90)=21.44µs  p(95)=37.36µs  p(99.9)=1.34ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.78ms min=17.41ms med=33.5ms  max=307.91ms p(90)=39.52ms  p(95)=41.21ms  p(99.9)=49.67ms
     http_reqs......................: 175838  1442.209079/s
     iteration_duration.............: avg=34.13ms min=20.97ms med=33.83ms max=320.08ms p(90)=39.85ms  p(95)=41.54ms  p(99.9)=50.1ms 
     iterations.....................: 175738  1441.388887/s
     success_rate...................: 100.00% ✓ 175738      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.363.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 521310      ✗ 0     
     data_received..................: 15 GB   125 MB/s
     data_sent......................: 209 MB  1.7 MB/s
     http_req_blocked...............: avg=3.01µs  min=961ns   med=2.14µs  max=3.85ms   p(90)=3.67µs  p(95)=4.35µs   p(99.9)=28.24µs 
     http_req_connecting............: avg=548ns   min=0s      med=0s      max=3.79ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.31ms min=17.88ms med=33.72ms max=301.32ms p(90)=40.93ms p(95)=43.28ms  p(99.9)=55.64ms 
       { expected_response:true }...: avg=34.31ms min=17.88ms med=33.72ms max=301.32ms p(90)=40.93ms p(95)=43.28ms  p(99.9)=55.64ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173870
     http_req_receiving.............: avg=68.93µs min=25.5µs  med=57.01µs max=113.98ms p(90)=94.81µs p(95)=111.15µs p(99.9)=683.12µs
     http_req_sending...............: avg=21.23µs min=4.76µs  med=10.19µs max=113.95ms p(90)=17.18µs p(95)=21.15µs  p(99.9)=745.56µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.22ms min=17.76ms med=33.64ms max=301.18ms p(90)=40.84ms p(95)=43.19ms  p(99.9)=55.41ms 
     http_reqs......................: 173870  1425.628444/s
     iteration_duration.............: avg=34.52ms min=20.11ms med=33.92ms max=312.76ms p(90)=41.12ms p(95)=43.47ms  p(99.9)=56.05ms 
     iterations.....................: 173770  1424.808505/s
     success_rate...................: 100.00% ✓ 173770      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 498759      ✗ 0     
     data_received..................: 15 GB   119 MB/s
     data_sent......................: 200 MB  1.6 MB/s
     http_req_blocked...............: avg=3.91µs  min=1.13µs  med=3.01µs  max=3.7ms    p(90)=4.63µs  p(95)=5.35µs   p(99.9)=37.78µs 
     http_req_connecting............: avg=581ns   min=0s      med=0s      max=3.66ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.85ms min=18.06ms med=35.32ms max=282.89ms p(90)=42.5ms  p(95)=44.89ms  p(99.9)=59.41ms 
       { expected_response:true }...: avg=35.85ms min=18.06ms med=35.32ms max=282.89ms p(90)=42.5ms  p(95)=44.89ms  p(99.9)=59.41ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 166353
     http_req_receiving.............: avg=73.57µs min=27.84µs med=60.86µs max=116.13ms p(90)=97.64µs p(95)=114.04µs p(99.9)=836.55µs
     http_req_sending...............: avg=24.66µs min=5.36µs  med=12.47µs max=110.75ms p(90)=18.44µs p(95)=22.14µs  p(99.9)=786.35µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=35.75ms min=18.01ms med=35.23ms max=282.54ms p(90)=42.4ms  p(95)=44.8ms   p(99.9)=59.02ms 
     http_reqs......................: 166353  1363.790221/s
     iteration_duration.............: avg=36.08ms min=21.59ms med=35.54ms max=306.01ms p(90)=42.71ms p(95)=45.1ms   p(99.9)=59.78ms 
     iterations.....................: 166253  1362.970404/s
     success_rate...................: 100.00% ✓ 166253      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 194340     ✗ 0    
     data_received..................: 5.7 GB  46 MB/s
     data_sent......................: 78 MB   638 kB/s
     http_req_blocked...............: avg=4.59µs  min=1.03µs  med=2.92µs  max=4.05ms   p(90)=4.39µs   p(95)=4.97µs   p(99.9)=51.47µs 
     http_req_connecting............: avg=1.43µs  min=0s      med=0s      max=4.01ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.27ms min=20.04ms med=90.47ms max=323.45ms p(90)=116.26ms p(95)=124.19ms p(99.9)=158.46ms
       { expected_response:true }...: avg=92.27ms min=20.04ms med=90.47ms max=323.45ms p(90)=116.26ms p(95)=124.19ms p(99.9)=158.46ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64880
     http_req_receiving.............: avg=78.52µs min=27.87µs med=71.57µs max=122.27ms p(90)=103.52µs p(95)=115.94µs p(99.9)=551.9µs 
     http_req_sending...............: avg=24.39µs min=5.11µs  med=14.32µs max=115.62ms p(90)=19.72µs  p(95)=21.85µs  p(99.9)=552.03µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.17ms min=19.95ms med=90.36ms max=322.92ms p(90)=116.17ms p(95)=124.09ms p(99.9)=158.12ms
     http_reqs......................: 64880   530.974238/s
     iteration_duration.............: avg=92.63ms min=27.68ms med=90.73ms max=338.36ms p(90)=116.52ms p(95)=124.44ms p(99.9)=159.73ms
     iterations.....................: 64780   530.155844/s
     success_rate...................: 100.00% ✓ 64780      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 190440     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 76 MB   625 kB/s
     http_req_blocked...............: avg=5.72µs  min=1.19µs  med=3.33µs  max=7.76ms   p(90)=4.86µs   p(95)=5.53µs   p(99.9)=46.39µs 
     http_req_connecting............: avg=1.94µs  min=0s      med=0s      max=7.35ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=94.15ms min=20.7ms  med=92.44ms max=312.51ms p(90)=111.99ms p(95)=121.25ms p(99.9)=220.73ms
       { expected_response:true }...: avg=94.15ms min=20.7ms  med=92.44ms max=312.51ms p(90)=111.99ms p(95)=121.25ms p(99.9)=220.73ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63580
     http_req_receiving.............: avg=81.19µs min=30.45µs med=74.56µs max=16.74ms  p(90)=108.07µs p(95)=120.46µs p(99.9)=520.78µs
     http_req_sending...............: avg=21.57µs min=5.43µs  med=14.91µs max=66.21ms  p(90)=20.65µs  p(95)=22.81µs  p(99.9)=632.78µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=94.05ms min=20.6ms  med=92.34ms max=311.37ms p(90)=111.89ms p(95)=121.14ms p(99.9)=220.58ms
     http_reqs......................: 63580   520.105447/s
     iteration_duration.............: avg=94.52ms min=34.66ms med=92.7ms  max=346.89ms p(90)=112.23ms p(95)=121.51ms p(99.9)=224ms   
     iterations.....................: 63480   519.287414/s
     success_rate...................: 100.00% ✓ 63480      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 153216     ✗ 0    
     data_received..................: 4.5 GB  37 MB/s
     data_sent......................: 61 MB   502 kB/s
     http_req_blocked...............: avg=4.89µs   min=1µs     med=3.03µs   max=3.56ms   p(90)=4.45µs   p(95)=4.98µs   p(99.9)=80.49µs 
     http_req_connecting............: avg=1.7µs    min=0s      med=0s       max=3.52ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=117.04ms min=20.34ms med=115.26ms max=343.5ms  p(90)=144.82ms p(95)=154.14ms p(99.9)=200.28ms
       { expected_response:true }...: avg=117.04ms min=20.34ms med=115.26ms max=343.5ms  p(90)=144.82ms p(95)=154.14ms p(99.9)=200.28ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 51172
     http_req_receiving.............: avg=95.94µs  min=27.53µs med=77.12µs  max=141.89ms p(90)=107.45µs p(95)=118.67µs p(99.9)=495.35µs
     http_req_sending...............: avg=21.31µs  min=4.85µs  med=14.98µs  max=64.84ms  p(90)=20.04µs  p(95)=22µs     p(99.9)=498.36µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=116.93ms min=20.2ms  med=115.15ms max=342.98ms p(90)=144.7ms  p(95)=154.02ms p(99.9)=199.37ms
     http_reqs......................: 51172   418.36132/s
     iteration_duration.............: avg=117.5ms  min=34.64ms med=115.55ms max=360.98ms p(90)=145.1ms  p(95)=154.43ms p(99.9)=204.01ms
     iterations.....................: 51072   417.543761/s
     success_rate...................: 100.00% ✓ 51072      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 97737      ✗ 0    
     data_received..................: 2.9 GB  23 MB/s
     data_sent......................: 39 MB   320 kB/s
     http_req_blocked...............: avg=5.6µs    min=1.1µs   med=2.88µs   max=3.32ms   p(90)=4.14µs   p(95)=4.66µs   p(99.9)=1.23ms  
     http_req_connecting............: avg=2.54µs   min=0s      med=0s       max=3.29ms   p(90)=0s       p(95)=0s       p(99.9)=1.21ms  
     http_req_duration..............: avg=183.47ms min=22.62ms med=183.28ms max=381.9ms  p(90)=195.48ms p(95)=200.62ms p(99.9)=264.95ms
       { expected_response:true }...: avg=183.47ms min=22.62ms med=183.28ms max=381.9ms  p(90)=195.48ms p(95)=200.62ms p(99.9)=264.95ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32679
     http_req_receiving.............: avg=90.17µs  min=32.16µs med=83.98µs  max=63.8ms   p(90)=113.15µs p(95)=123.57µs p(99.9)=479.53µs
     http_req_sending...............: avg=26.6µs   min=4.91µs  med=16.25µs  max=61.25ms  p(90)=20.14µs  p(95)=21.71µs  p(99.9)=457.57µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=183.36ms min=22.44ms med=183.19ms max=379.53ms p(90)=195.37ms p(95)=200.5ms  p(99.9)=264.86ms
     http_reqs......................: 32679   266.629503/s
     iteration_duration.............: avg=184.24ms min=42.91ms med=183.62ms max=390.59ms p(90)=195.75ms p(95)=200.91ms p(99.9)=266.27ms
     iterations.....................: 32579   265.813598/s
     success_rate...................: 100.00% ✓ 32579      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 96891      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   318 kB/s
     http_req_blocked...............: avg=6.61µs   min=1.52µs  med=3.55µs   max=4.1ms    p(90)=5.02µs   p(95)=5.63µs   p(99.9)=1.09ms  
     http_req_connecting............: avg=2.77µs   min=0s      med=0s       max=4.05ms   p(90)=0s       p(95)=0s       p(99.9)=1.07ms  
     http_req_duration..............: avg=185.07ms min=17.94ms med=171.33ms max=772.19ms p(90)=217.75ms p(95)=238.23ms p(99.9)=680.38ms
       { expected_response:true }...: avg=185.07ms min=17.94ms med=171.33ms max=772.19ms p(90)=217.75ms p(95)=238.23ms p(99.9)=680.38ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32397
     http_req_receiving.............: avg=98.56µs  min=36.09µs med=88.39µs  max=85.39ms  p(90)=119.08µs p(95)=131.35µs p(99.9)=788.51µs
     http_req_sending...............: avg=30µs     min=6.44µs  med=18.16µs  max=161.46ms p(90)=22.95µs  p(95)=24.82µs  p(99.9)=547.51µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.94ms min=17.86ms med=171.22ms max=772.06ms p(90)=217.63ms p(95)=237.97ms p(99.9)=680.28ms
     http_reqs......................: 32397   265.032594/s
     iteration_duration.............: avg=185.87ms min=36.36ms med=171.71ms max=772.45ms p(90)=218.15ms p(95)=238.78ms p(99.9)=680.72ms
     iterations.....................: 32297   264.214516/s
     success_rate...................: 100.00% ✓ 32297      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

