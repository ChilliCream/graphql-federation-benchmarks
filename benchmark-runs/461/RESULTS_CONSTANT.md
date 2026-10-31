## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 5,168 | 5,176 | 5,126 | 0.4% | 369 MB | 73.1 KB |  |
| fusion-net-11 | 16.7.3 | 5,028 | 5,036 | 5,018 | 0.1% | 382 MB | 77.8 KB |  |
| fusion-aot-11 | 16.7.3 | 4,888 | 4,896 | 4,881 | 0.1% | 148 MB | 31.0 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,871 | 4,898 | 4,844 | 0.4% | 122 MB | 25.6 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,849 | 4,886 | 4,840 | 0.4% | 382 MB | 80.8 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,795 | 4,824 | 4,764 | 0.5% | 392 MB | 83.7 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,504 | 4,507 | 4,486 | 0.2% | 126 MB | 28.6 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,493 | 4,520 | 4,468 | 0.5% | 122 MB | 27.8 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,263 | 4,405 | 4,139 | 2.7% | 2,313 MB | 555.5 KB |  |
| hive-router | v0.3.6 | 2,881 | 2,912 | 2,856 | 0.7% | 90 MB | 32.1 KB |  |
| grafbase | 0.53.5 | 1,892 | 1,898 | 1,885 | 0.2% | 109 MB | 58.9 KB |  |
| cosmo | 0.363.0 | 1,497 | 1,498 | 1,495 | 0.1% | 163 MB | 111.2 KB |  |
| caliban | 3.2.0 | 1,415 | 1,416 | 1,415 | 0.0% | 5,081 MB | 3,677.0 KB |  |
| hive-gateway-router-runtime | 2.15.3 | 541 | 543 | 539 | 0.3% | 2,747 MB | 5,199.1 KB |  |
| apollo-router | v2.19.0 | 509 | 516 | 503 | 0.9% | 173 MB | 348.5 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 398 | 399 | 398 | 0.1% | 202 MB | 520.4 KB |  |
| apollo-gateway | 2.14.4 | 279 | 280 | 275 | 0.8% | 2,169 MB | 7,962.5 KB |  |
| hive-gateway | 2.15.3 | 260 | 261 | 258 | 0.4% | 3,442 MB | 13,558.0 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1861950     ✗ 0     
     data_received..................: 54 GB   452 MB/s
     data_sent......................: 746 MB  6.2 MB/s
     http_req_blocked...............: avg=2.88µs  min=802ns    med=1.93µs  max=11.85ms  p(90)=3.03µs  p(95)=3.63µs   p(99.9)=27.28µs
     http_req_connecting............: avg=481ns   min=0s       med=0s      max=8.8ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.45ms  min=779.26µs med=8.61ms  max=203.17ms p(90)=14.66ms p(95)=17.48ms  p(99.9)=29.75ms
       { expected_response:true }...: avg=9.45ms  min=779.26µs med=8.61ms  max=203.17ms p(90)=14.66ms p(95)=17.48ms  p(99.9)=29.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 620750
     http_req_receiving.............: avg=91.2µs  min=24.1µs   med=44.73µs max=40.26ms  p(90)=86.45µs p(95)=184.39µs p(99.9)=6.27ms 
     http_req_sending...............: avg=41.35µs min=4.55µs   med=8.18µs  max=44.24ms  p(90)=14.31µs p(95)=97.31µs  p(99.9)=4.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.32ms  min=735.34µs med=8.5ms   max=200.83ms p(90)=14.45ms p(95)=17.22ms  p(99.9)=29.26ms
     http_reqs......................: 620750  5168.337548/s
     iteration_duration.............: avg=9.65ms  min=1.18ms   med=8.79ms  max=372.09ms p(90)=14.86ms p(95)=17.69ms  p(99.9)=30.08ms
     iterations.....................: 620650  5167.504953/s
     success_rate...................: 100.00% ✓ 620650      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1811790     ✗ 0     
     data_received..................: 53 GB   440 MB/s
     data_sent......................: 726 MB  6.0 MB/s
     http_req_blocked...............: avg=2.67µs  min=831ns    med=1.87µs  max=10.08ms  p(90)=2.89µs  p(95)=3.45µs   p(99.9)=25.4µs 
     http_req_connecting............: avg=411ns   min=0s       med=0s      max=10.05ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.73ms  min=836.89µs med=8.96ms  max=314.73ms p(90)=14.84ms p(95)=17.44ms  p(99.9)=28.86ms
       { expected_response:true }...: avg=9.73ms  min=836.89µs med=8.96ms  max=314.73ms p(90)=14.84ms p(95)=17.44ms  p(99.9)=28.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 604030
     http_req_receiving.............: avg=88.06µs min=24.25µs  med=45.65µs max=145.58ms p(90)=84.86µs p(95)=188.67µs p(99.9)=5.57ms 
     http_req_sending...............: avg=40µs    min=4.24µs   med=8.03µs  max=157.29ms p(90)=13.75µs p(95)=97.23µs  p(99.9)=4.29ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.6ms   min=786.14µs med=8.86ms  max=313.69ms p(90)=14.64ms p(95)=17.21ms  p(99.9)=28.43ms
     http_reqs......................: 604030  5028.923487/s
     iteration_duration.............: avg=9.92ms  min=984.32µs med=9.15ms  max=326.97ms p(90)=15.04ms p(95)=17.65ms  p(99.9)=29.12ms
     iterations.....................: 603930  5028.090925/s
     success_rate...................: 100.00% ✓ 603930      ✗ 0     
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

     checks.........................: 100.00% ✓ 1761360     ✗ 0     
     data_received..................: 51 GB   428 MB/s
     data_sent......................: 706 MB  5.9 MB/s
     http_req_blocked...............: avg=2.44µs  min=791ns    med=1.88µs  max=9.12ms   p(90)=3.01µs  p(95)=3.62µs   p(99.9)=26.78µs
     http_req_connecting............: avg=152ns   min=0s       med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.02ms min=913.95µs med=9.33ms  max=258.98ms p(90)=14.91ms p(95)=17.43ms  p(99.9)=28.71ms
       { expected_response:true }...: avg=10.02ms min=913.95µs med=9.33ms  max=258.98ms p(90)=14.91ms p(95)=17.43ms  p(99.9)=28.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 587220
     http_req_receiving.............: avg=89.81µs min=23.92µs  med=43.76µs max=178.96ms p(90)=89.6µs  p(95)=196.8µs  p(99.9)=5.68ms 
     http_req_sending...............: avg=38.89µs min=4.3µs    med=7.99µs  max=191.86ms p(90)=14.65µs p(95)=101.87µs p(99.9)=3.87ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.89ms  min=838.19µs med=9.23ms  max=258.53ms p(90)=14.71ms p(95)=17.18ms  p(99.9)=28.24ms
     http_reqs......................: 587220  4888.589395/s
     iteration_duration.............: avg=10.21ms min=1.1ms    med=9.51ms  max=280.61ms p(90)=15.1ms  p(95)=17.64ms  p(99.9)=28.96ms
     iterations.....................: 587120  4887.756897/s
     success_rate...................: 100.00% ✓ 587120      ✗ 0     
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

     checks.........................: 100.00% ✓ 1755009     ✗ 0     
     data_received..................: 51 GB   426 MB/s
     data_sent......................: 703 MB  5.9 MB/s
     http_req_blocked...............: avg=2.39µs  min=791ns    med=1.87µs  max=3.88ms   p(90)=3.05µs  p(95)=3.66µs   p(99.9)=25.38µs
     http_req_connecting............: avg=151ns   min=0s       med=0s      max=3.4ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.05ms min=903.68µs med=9.38ms  max=276.47ms p(90)=14.93ms p(95)=17.42ms  p(99.9)=28.68ms
       { expected_response:true }...: avg=10.05ms min=903.68µs med=9.38ms  max=276.47ms p(90)=14.93ms p(95)=17.42ms  p(99.9)=28.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 585103
     http_req_receiving.............: avg=88.83µs min=23.4µs   med=43.69µs max=194.97ms p(90)=89.16µs p(95)=196.95µs p(99.9)=5.48ms 
     http_req_sending...............: avg=38.66µs min=4.22µs   med=7.92µs  max=187.73ms p(90)=14.24µs p(95)=101.23µs p(99.9)=3.83ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.93ms  min=834.46µs med=9.27ms  max=265.15ms p(90)=14.74ms p(95)=17.19ms  p(99.9)=28.32ms
     http_reqs......................: 585103  4871.073842/s
     iteration_duration.............: avg=10.24ms min=1.54ms   med=9.56ms  max=286.13ms p(90)=15.13ms p(95)=17.62ms  p(99.9)=28.91ms
     iterations.....................: 585003  4870.241326/s
     success_rate...................: 100.00% ✓ 585003      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1747443     ✗ 0     
     data_received..................: 51 GB   424 MB/s
     data_sent......................: 700 MB  5.8 MB/s
     http_req_blocked...............: avg=3.06µs   min=972ns    med=2.42µs  max=9.44ms   p(90)=3.81µs  p(95)=4.6µs    p(99.9)=34.88µs
     http_req_connecting............: avg=155ns    min=0s       med=0s      max=3.97ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.08ms  min=959.25µs med=9.16ms  max=281.81ms p(90)=15.65ms p(95)=18.68ms  p(99.9)=31.88ms
       { expected_response:true }...: avg=10.08ms  min=959.25µs med=9.16ms  max=281.81ms p(90)=15.65ms p(95)=18.68ms  p(99.9)=31.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 582581
     http_req_receiving.............: avg=105.12µs min=25.13µs  med=49.03µs max=150.4ms  p(90)=99.85µs p(95)=206.12µs p(99.9)=7.11ms 
     http_req_sending...............: avg=45.76µs  min=4.28µs   med=8.72µs  max=143.77ms p(90)=16.75µs p(95)=107.86µs p(99.9)=5.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.92ms   min=910.97µs med=9.04ms  max=281.34ms p(90)=15.4ms  p(95)=18.38ms  p(99.9)=31.34ms
     http_reqs......................: 582581  4849.754607/s
     iteration_duration.............: avg=10.28ms  min=1.38ms   med=9.36ms  max=292.73ms p(90)=15.87ms p(95)=18.91ms  p(99.9)=32.17ms
     iterations.....................: 582481  4848.922147/s
     success_rate...................: 100.00% ✓ 582481      ✗ 0     
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

     checks.........................: 100.00% ✓ 1727865     ✗ 0     
     data_received..................: 50 GB   420 MB/s
     data_sent......................: 692 MB  5.8 MB/s
     http_req_blocked...............: avg=2.57µs  min=792ns    med=1.96µs max=12.4ms   p(90)=3.07µs  p(95)=3.74µs  p(99.9)=27.52µs
     http_req_connecting............: avg=150ns   min=0s       med=0s     max=3.65ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=10.2ms  min=996.03µs med=9.47ms max=284.85ms p(90)=15.4ms  p(95)=17.95ms p(99.9)=30.28ms
       { expected_response:true }...: avg=10.2ms  min=996.03µs med=9.47ms max=284.85ms p(90)=15.4ms  p(95)=17.95ms p(99.9)=30.28ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 576055
     http_req_receiving.............: avg=94.75µs min=25.26µs  med=47.6µs max=34.66ms  p(90)=92.15µs p(95)=193.9µs p(99.9)=5.98ms 
     http_req_sending...............: avg=42.26µs min=4.54µs   med=8.41µs max=76.07ms  p(90)=14.89µs p(95)=98.25µs p(99.9)=4.78ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=10.06ms min=933.21µs med=9.35ms max=283.9ms  p(90)=15.2ms  p(95)=17.72ms p(99.9)=29.9ms 
     http_reqs......................: 576055  4795.301758/s
     iteration_duration.............: avg=10.4ms  min=1.26ms   med=9.66ms max=292.95ms p(90)=15.61ms p(95)=18.17ms p(99.9)=30.56ms
     iterations.....................: 575955  4794.46932/s
     success_rate...................: 100.00% ✓ 575955      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1623063     ✗ 0     
     data_received..................: 47 GB   394 MB/s
     data_sent......................: 650 MB  5.4 MB/s
     http_req_blocked...............: avg=2.91µs  min=802ns   med=1.96µs  max=87.92ms  p(90)=3.12µs  p(95)=3.76µs   p(99.9)=27.02µs
     http_req_connecting............: avg=553ns   min=0s      med=0s      max=87.86ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.88ms min=1.07ms  med=10.31ms max=281.02ms p(90)=15.71ms p(95)=18.08ms  p(99.9)=29.88ms
       { expected_response:true }...: avg=10.88ms min=1.07ms  med=10.31ms max=281.02ms p(90)=15.71ms p(95)=18.08ms  p(99.9)=29.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 541121
     http_req_receiving.............: avg=96.35µs min=25.07µs med=46.93µs max=96.03ms  p(90)=94.62µs p(95)=204.31µs p(99.9)=6.19ms 
     http_req_sending...............: avg=41.62µs min=4.57µs  med=8.26µs  max=202.24ms p(90)=15.27µs p(95)=102.65µs p(99.9)=4.14ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.74ms min=998.3µs med=10.2ms  max=268.96ms p(90)=15.51ms p(95)=17.84ms  p(99.9)=29.46ms
     http_reqs......................: 541121  4504.210148/s
     iteration_duration.............: avg=11.08ms min=1.69ms  med=10.5ms  max=290.18ms p(90)=15.91ms p(95)=18.29ms  p(99.9)=30.17ms
     iterations.....................: 541021  4503.377763/s
     success_rate...................: 100.00% ✓ 541021      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1619370     ✗ 0     
     data_received..................: 47 GB   393 MB/s
     data_sent......................: 649 MB  5.4 MB/s
     http_req_blocked...............: avg=2.85µs   min=792ns   med=1.92µs  max=8.99ms   p(90)=3.05µs  p(95)=3.67µs   p(99.9)=25.28µs
     http_req_connecting............: avg=520ns    min=0s      med=0s      max=8.95ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.91ms  min=1.1ms   med=10.37ms max=324.1ms  p(90)=15.68ms p(95)=17.9ms   p(99.9)=29.31ms
       { expected_response:true }...: avg=10.91ms  min=1.1ms   med=10.37ms max=324.1ms  p(90)=15.68ms p(95)=17.9ms   p(99.9)=29.31ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 539890
     http_req_receiving.............: avg=102.99µs min=23.49µs med=46.13µs max=231.96ms p(90)=95.2µs  p(95)=208.73µs p(99.9)=6.3ms  
     http_req_sending...............: avg=39.35µs  min=4.26µs  med=8.12µs  max=248.49ms p(90)=15.09µs p(95)=101.73µs p(99.9)=3.83ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.76ms  min=1.01ms  med=10.26ms max=112.12ms p(90)=15.48ms p(95)=17.67ms  p(99.9)=28.69ms
     http_reqs......................: 539890  4493.88717/s
     iteration_duration.............: avg=11.1ms   min=1.58ms  med=10.56ms max=353.48ms p(90)=15.88ms p(95)=18.11ms  p(99.9)=29.66ms
     iterations.....................: 539790  4493.054799/s
     success_rate...................: 100.00% ✓ 539790      ✗ 0     
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

     checks.........................: 100.00% ✓ 1536270     ✗ 0     
     data_received..................: 45 GB   373 MB/s
     data_sent......................: 616 MB  5.1 MB/s
     http_req_blocked...............: avg=3µs     min=881ns    med=2.44µs  max=5.18ms   p(90)=3.77µs  p(95)=4.42µs   p(99.9)=32.98µs
     http_req_connecting............: avg=169ns   min=0s       med=0s      max=3.42ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=11.51ms min=789.24µs med=11.07ms max=300.21ms p(90)=16.89ms p(95)=19.31ms  p(99.9)=30.69ms
       { expected_response:true }...: avg=11.51ms min=789.24µs med=11.07ms max=300.21ms p(90)=16.89ms p(95)=19.31ms  p(99.9)=30.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 512190
     http_req_receiving.............: avg=88.85µs min=24.99µs  med=49.19µs max=17.24ms  p(90)=96.44µs p(95)=218.43µs p(99.9)=4.45ms 
     http_req_sending...............: avg=42.16µs min=4.41µs   med=9.22µs  max=132.94ms p(90)=16.29µs p(95)=117.6µs  p(99.9)=3.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=11.37ms min=746.97µs med=10.95ms max=299.59ms p(90)=16.72ms p(95)=19.08ms  p(99.9)=30.35ms
     http_reqs......................: 512190  4263.940086/s
     iteration_duration.............: avg=11.7ms  min=1.24ms   med=11.26ms max=310.26ms p(90)=17.1ms  p(95)=19.52ms  p(99.9)=30.93ms
     iterations.....................: 512090  4263.107594/s
     success_rate...................: 100.00% ✓ 512090      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 1038345     ✗ 0     
     data_received..................: 30 GB   252 MB/s
     data_sent......................: 416 MB  3.5 MB/s
     http_req_blocked...............: avg=2.51µs  min=861ns   med=2.09µs  max=1.92ms   p(90)=3.4µs   p(95)=4.06µs   p(99.9)=28.23µs
     http_req_connecting............: avg=120ns   min=0s      med=0s      max=1.87ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.13ms min=1.21ms  med=17.21ms max=269.42ms p(90)=22.95ms p(95)=24.48ms  p(99.9)=31.44ms
       { expected_response:true }...: avg=17.13ms min=1.21ms  med=17.21ms max=269.42ms p(90)=22.95ms p(95)=24.48ms  p(99.9)=31.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 346215
     http_req_receiving.............: avg=69.94µs min=23.18µs med=50.91µs max=165.44ms p(90)=88.13µs p(95)=130.37µs p(99.9)=1.1ms  
     http_req_sending...............: avg=30.07µs min=4.37µs  med=9.32µs  max=126.11ms p(90)=15.5µs  p(95)=91.68µs  p(99.9)=1.16ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.03ms min=1.17ms  med=17.11ms max=269.16ms p(90)=22.84ms p(95)=24.38ms  p(99.9)=31.32ms
     http_reqs......................: 346215  2881.004608/s
     iteration_duration.............: avg=17.32ms min=2.9ms   med=17.39ms max=281.98ms p(90)=23.13ms p(95)=24.67ms  p(99.9)=31.63ms
     iterations.....................: 346115  2880.172465/s
     success_rate...................: 100.00% ✓ 346115      ✗ 0     
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

     checks.........................: 100.00% ✓ 682587      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 274 MB  2.3 MB/s
     http_req_blocked...............: avg=3.92µs  min=902ns   med=2.29µs  max=8.7ms    p(90)=4.44µs   p(95)=5.51µs   p(99.9)=39.51µs
     http_req_connecting............: avg=1.07µs  min=0s      med=0s      max=8.57ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.12ms min=1.84ms  med=25.59ms max=301.17ms p(90)=33.85ms  p(95)=36.64ms  p(99.9)=50.48ms
       { expected_response:true }...: avg=26.12ms min=1.84ms  med=25.59ms max=301.17ms p(90)=33.85ms  p(95)=36.64ms  p(99.9)=50.48ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 227629
     http_req_receiving.............: avg=84.35µs min=27.33µs med=56.86µs max=154.31ms p(90)=118.51µs p(95)=181.3µs  p(99.9)=1.56ms 
     http_req_sending...............: avg=32.37µs min=4.65µs  med=9.8µs   max=213.35ms p(90)=22.06µs  p(95)=100.22µs p(99.9)=1.41ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.01ms min=1.79ms  med=25.48ms max=299.66ms p(90)=33.72ms  p(95)=36.51ms  p(99.9)=50.09ms
     http_reqs......................: 227629  1892.944553/s
     iteration_duration.............: avg=26.36ms min=8.27ms  med=25.81ms max=328.07ms p(90)=34.07ms  p(95)=36.86ms  p(99.9)=50.8ms 
     iterations.....................: 227529  1892.112961/s
     success_rate...................: 100.00% ✓ 227529      ✗ 0     
     vus............................: 50      min=50        max=50  
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

     checks.........................: 100.00% ✓ 539988      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 216 MB  1.8 MB/s
     http_req_blocked...............: avg=2.76µs  min=862ns   med=1.98µs  max=3.1ms    p(90)=3.34µs  p(95)=3.97µs   p(99.9)=29.52µs 
     http_req_connecting............: avg=468ns   min=0s      med=0s      max=3.05ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=33.11ms min=2.02ms  med=32.22ms max=279.79ms p(90)=47.84ms p(95)=52.7ms   p(99.9)=75.59ms 
       { expected_response:true }...: avg=33.11ms min=2.02ms  med=32.22ms max=279.79ms p(90)=47.84ms p(95)=52.7ms   p(99.9)=75.59ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 180096
     http_req_receiving.............: avg=69.39µs min=26.52µs med=58.65µs max=85.66ms  p(90)=93.78µs p(95)=109.43µs p(99.9)=681.01µs
     http_req_sending...............: avg=20.2µs  min=4.59µs  med=9.89µs  max=101.86ms p(90)=16.25µs p(95)=19.96µs  p(99.9)=739.64µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=33.02ms min=1.93ms  med=32.13ms max=278.94ms p(90)=47.76ms p(95)=52.61ms  p(99.9)=75.34ms 
     http_reqs......................: 180096  1497.356795/s
     iteration_duration.............: avg=33.32ms min=4.36ms  med=32.41ms max=298.79ms p(90)=48.04ms p(95)=52.88ms  p(99.9)=75.93ms 
     iterations.....................: 179996  1496.525373/s
     success_rate...................: 100.00% ✓ 179996      ✗ 0     
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

     checks.........................: 100.00% ✓ 510411      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 205 MB  1.7 MB/s
     http_req_blocked...............: avg=3.18µs  min=982ns  med=2.34µs  max=4.05ms   p(90)=3.9µs   p(95)=4.59µs   p(99.9)=31.26µs 
     http_req_connecting............: avg=537ns   min=0s     med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=35.03ms min=2.05ms med=34.05ms max=277.67ms p(90)=49.88ms p(95)=55.03ms  p(99.9)=83.19ms 
       { expected_response:true }...: avg=35.03ms min=2.05ms med=34.05ms max=277.67ms p(90)=49.88ms p(95)=55.03ms  p(99.9)=83.19ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 170237
     http_req_receiving.............: avg=70.52µs min=26.8µs med=57.49µs max=133.19ms p(90)=91.36µs p(95)=105.85µs p(99.9)=745.45µs
     http_req_sending...............: avg=19.82µs min=4.84µs med=10.9µs  max=106.31ms p(90)=17.25µs p(95)=20.52µs  p(99.9)=697.92µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.94ms min=1.99ms med=33.97ms max=257.95ms p(90)=49.79ms p(95)=54.95ms  p(99.9)=82.97ms 
     http_reqs......................: 170237  1415.370012/s
     iteration_duration.............: avg=35.25ms min=5.79ms med=34.26ms max=305.65ms p(90)=50.08ms p(95)=55.24ms  p(99.9)=83.84ms 
     iterations.....................: 170137  1414.5386/s
     success_rate...................: 100.00% ✓ 170137      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
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

     checks.........................: 100.00% ✓ 195396     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   650 kB/s
     http_req_blocked...............: avg=4.75µs  min=1.14µs med=2.99µs  max=3.67ms   p(90)=4.42µs   p(95)=5.04µs   p(99.9)=45.67µs 
     http_req_connecting............: avg=1.51µs  min=0s     med=0s      max=3.63ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=91.76ms min=3.97ms med=89.03ms max=340.33ms p(90)=110.83ms p(95)=121.87ms p(99.9)=223.09ms
       { expected_response:true }...: avg=91.76ms min=3.97ms med=89.03ms max=340.33ms p(90)=110.83ms p(95)=121.87ms p(99.9)=223.09ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 65232
     http_req_receiving.............: avg=81.82µs min=30.1µs med=71.11µs max=86.8ms   p(90)=104.03µs p(95)=115.86µs p(99.9)=532.37µs
     http_req_sending...............: avg=19.47µs min=5.44µs med=13.95µs max=35.38ms  p(90)=19.74µs  p(95)=21.78µs  p(99.9)=570.05µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=91.66ms min=3.85ms med=88.93ms max=339.78ms p(90)=110.73ms p(95)=121.74ms p(99.9)=222.76ms
     http_reqs......................: 65232   541.1163/s
     iteration_duration.............: avg=92.14ms min=23ms   med=89.28ms max=349.38ms p(90)=111.08ms p(95)=122.16ms p(99.9)=224.33ms
     iterations.....................: 65132   540.286774/s
     success_rate...................: 100.00% ✓ 65132      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 183930     ✗ 0    
     data_received..................: 5.4 GB  45 MB/s
     data_sent......................: 74 MB   612 kB/s
     http_req_blocked...............: avg=4.35µs  min=982ns   med=2.75µs  max=3.41ms   p(90)=4.19µs   p(95)=4.77µs   p(99.9)=49.62µs 
     http_req_connecting............: avg=1.41µs  min=0s      med=0s      max=3.37ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=97.47ms min=4.43ms  med=95.53ms max=334.07ms p(90)=131.66ms p(95)=141.94ms p(99.9)=185.59ms
       { expected_response:true }...: avg=97.47ms min=4.43ms  med=95.53ms max=334.07ms p(90)=131.66ms p(95)=141.94ms p(99.9)=185.59ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 61410
     http_req_receiving.............: avg=77.46µs min=29.63µs med=71.4µs  max=113.09ms p(90)=101.75µs p(95)=114.12µs p(99.9)=518.61µs
     http_req_sending...............: avg=20.6µs  min=5.17µs  med=13.83µs max=72.59ms  p(90)=19.24µs  p(95)=21.09µs  p(99.9)=489.65µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=97.37ms min=4.37ms  med=95.43ms max=328.99ms p(90)=131.55ms p(95)=141.83ms p(99.9)=185.35ms
     http_reqs......................: 61410   509.308326/s
     iteration_duration.............: avg=97.87ms min=20.87ms med=95.79ms max=342.82ms p(90)=131.92ms p(95)=142.19ms p(99.9)=188.92ms
     iterations.....................: 61310   508.478969/s
     success_rate...................: 100.00% ✓ 61310      ✗ 0    
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

     checks.........................: 100.00% ✓ 144123     ✗ 0    
     data_received..................: 4.2 GB  35 MB/s
     data_sent......................: 58 MB   479 kB/s
     http_req_blocked...............: avg=4.59µs   min=1.01µs  med=2.68µs   max=3.41ms   p(90)=3.98µs   p(95)=4.51µs   p(99.9)=164.11µs
     http_req_connecting............: avg=1.75µs   min=0s      med=0s       max=3.37ms   p(90)=0s       p(95)=0s       p(99.9)=84.26µs 
     http_req_duration..............: avg=124.44ms min=5.4ms   med=121.94ms max=318.46ms p(90)=163ms    p(95)=175.56ms p(99.9)=228.56ms
       { expected_response:true }...: avg=124.44ms min=5.4ms   med=121.94ms max=318.46ms p(90)=163ms    p(95)=175.56ms p(99.9)=228.56ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48141
     http_req_receiving.............: avg=79.02µs  min=28.77µs med=72.17µs  max=174.91ms p(90)=101.18µs p(95)=112.97µs p(99.9)=419.75µs
     http_req_sending...............: avg=24.63µs  min=4.94µs  med=13.65µs  max=97.05ms  p(90)=18.51µs  p(95)=20.07µs  p(99.9)=433.79µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=124.34ms min=5.3ms   med=121.85ms max=308.28ms p(90)=162.9ms  p(95)=175.44ms p(99.9)=227.95ms
     http_reqs......................: 48141   398.856662/s
     iteration_duration.............: avg=124.93ms min=35.16ms med=122.24ms max=326.01ms p(90)=163.28ms p(95)=175.83ms p(99.9)=230.23ms
     iterations.....................: 48041   398.028145/s
     success_rate...................: 100.00% ✓ 48041      ✗ 0    
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

     checks.........................: 100.00% ✓ 101274     ✗ 0    
     data_received..................: 3.0 GB  25 MB/s
     data_sent......................: 41 MB   336 kB/s
     http_req_blocked...............: avg=5.98µs   min=1.1µs   med=3.13µs   max=4.22ms   p(90)=4.44µs   p(95)=5.02µs   p(99.9)=1.01ms  
     http_req_connecting............: avg=2.65µs   min=0s      med=0s       max=4.18ms   p(90)=0s       p(95)=0s       p(99.9)=995.95µs
     http_req_duration..............: avg=177.05ms min=7.33ms  med=170.49ms max=391.11ms p(90)=201.66ms p(95)=208.39ms p(99.9)=280.06ms
       { expected_response:true }...: avg=177.05ms min=7.33ms  med=170.49ms max=391.11ms p(90)=201.66ms p(95)=208.39ms p(99.9)=280.06ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 33858
     http_req_receiving.............: avg=89.27µs  min=29.53µs med=83.88µs  max=70.21ms  p(90)=113.16µs p(95)=124.09µs p(99.9)=519.39µs
     http_req_sending...............: avg=25.42µs  min=5.06µs  med=15.79µs  max=85.32ms  p(90)=20.02µs  p(95)=22.07µs  p(99.9)=544.89µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=176.93ms min=7.25ms  med=170.38ms max=390.66ms p(90)=201.55ms p(95)=208.26ms p(99.9)=279.81ms
     http_reqs......................: 33858   279.949337/s
     iteration_duration.............: avg=177.83ms min=46.02ms med=170.74ms max=409.87ms p(90)=201.94ms p(95)=208.67ms p(99.9)=281.22ms
     iterations.....................: 33758   279.122503/s
     success_rate...................: 100.00% ✓ 33758      ✗ 0    
     vus............................: 50      min=50       max=50 
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

     checks.........................: 100.00% ✓ 94098      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   313 kB/s
     http_req_blocked...............: avg=6.58µs   min=1.07µs  med=3.34µs   max=3.45ms   p(90)=4.64µs   p(95)=5.2µs    p(99.9)=1.57ms  
     http_req_connecting............: avg=2.99µs   min=0s      med=0s       max=3.41ms   p(90)=0s       p(95)=0s       p(99.9)=1.54ms  
     http_req_duration..............: avg=190.56ms min=5.9ms   med=173.62ms max=763.78ms p(90)=220.43ms p(95)=254.79ms p(99.9)=673.82ms
       { expected_response:true }...: avg=190.56ms min=5.9ms   med=173.62ms max=763.78ms p(90)=220.43ms p(95)=254.79ms p(99.9)=673.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31466
     http_req_receiving.............: avg=113.97µs min=34.26µs med=83.04µs  max=111.71ms p(90)=111.89µs p(95)=122.78µs p(99.9)=755.59µs
     http_req_sending...............: avg=24.96µs  min=5.55µs  med=16.37µs  max=130.86ms p(90)=20.59µs  p(95)=22.21µs  p(99.9)=468.87µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=190.42ms min=5.82ms  med=173.51ms max=763.69ms p(90)=220.17ms p(95)=254.1ms  p(99.9)=673.71ms
     http_reqs......................: 31466   260.244277/s
     iteration_duration.............: avg=191.4ms  min=93.54ms med=173.93ms max=763.97ms p(90)=220.82ms p(95)=255.76ms p(99.9)=674.1ms 
     iterations.....................: 31366   259.417212/s
     success_rate...................: 100.00% ✓ 31366      ✗ 0    
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

