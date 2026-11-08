## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.9 | 3,415 | 3,425 | 3,408 | 0.2% | 394 MB | 118.1 KB |  |
| fusion-net-11 | 16.7.3 | 3,404 | 3,405 | 3,392 | 0.2% | 387 MB | 116.5 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 3,351 | 3,367 | 3,338 | 0.4% | 129 MB | 39.4 KB |  |
| fusion-aot-11 | 16.7.3 | 3,348 | 3,391 | 3,344 | 0.6% | 129 MB | 39.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 3,265 | 3,278 | 3,242 | 0.4% | 2,305 MB | 722.8 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 2,804 | 2,810 | 2,796 | 0.2% | 387 MB | 141.5 KB |  |
| fusion-fed-net-11 | 16.7.3 | 2,797 | 2,799 | 2,790 | 0.1% | 396 MB | 145.1 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 2,745 | 2,751 | 2,736 | 0.2% | 146 MB | 54.4 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 2,743 | 2,749 | 2,737 | 0.2% | 133 MB | 49.5 KB |  |
| hive-router | v0.3.10 | 2,056 | 2,066 | 2,046 | 0.4% | 90 MB | 44.8 KB |  |
| caliban | 3.2.0 | 1,499 | 1,502 | 1,498 | 0.1% | 5,041 MB | 3,443.9 KB |  |
| grafbase | 0.53.5 | 1,442 | 1,451 | 1,433 | 0.5% | 101 MB | 71.6 KB |  |
| cosmo | 0.365.2 | 1,412 | 1,413 | 1,409 | 0.1% | 151 MB | 109.3 KB |  |
| apollo-router | v2.19.0 | 529 | 530 | 529 | 0.1% | 180 MB | 348.8 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 520 | 522 | 520 | 0.2% | 2,748 MB | 5,412.4 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 412 | 417 | 407 | 0.9% | 204 MB | 506.0 KB |  |
| hive-gateway | 2.15.6 | 265 | 266 | 263 | 0.4% | 3,677 MB | 14,209.0 KB |  |
| apollo-gateway | 2.14.4 | 262 | 262 | 260 | 0.3% | 2,165 MB | 8,463.6 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.9)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1239006     ✗ 0     
     data_received..................: 36 GB   299 MB/s
     data_sent......................: 496 MB  4.1 MB/s
     http_req_blocked...............: avg=2.49µs  min=801ns   med=1.82µs  max=6.23ms   p(90)=3.08µs  p(95)=3.88µs   p(99.9)=23.19µs
     http_req_connecting............: avg=276ns   min=0s      med=0s      max=6.15ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.32ms min=8.19ms  med=13.91ms max=276.23ms p(90)=17.77ms p(95)=19.14ms  p(99.9)=26.7ms 
       { expected_response:true }...: avg=14.32ms min=8.19ms  med=13.91ms max=276.23ms p(90)=17.77ms p(95)=19.14ms  p(99.9)=26.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 413102
     http_req_receiving.............: avg=69.57µs min=24.01µs med=43.1µs  max=121.59ms p(90)=93.02µs p(95)=167.01µs p(99.9)=1.95ms 
     http_req_sending...............: avg=31.23µs min=4.14µs  med=7.69µs  max=170.84ms p(90)=16.67µs p(95)=89.76µs  p(99.9)=2.01ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.22ms min=8.14ms  med=13.81ms max=276.06ms p(90)=17.67ms p(95)=19.02ms  p(99.9)=26.43ms
     http_reqs......................: 413102  3415.455338/s
     iteration_duration.............: avg=14.51ms min=8.38ms  med=14.1ms  max=294.28ms p(90)=17.96ms p(95)=19.33ms  p(99.9)=26.9ms 
     iterations.....................: 413002  3414.628556/s
     success_rate...................: 100.00% ✓ 413002      ✗ 0     
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

     checks.........................: 100.00% ✓ 1235004     ✗ 0     
     data_received..................: 36 GB   298 MB/s
     data_sent......................: 495 MB  4.1 MB/s
     http_req_blocked...............: avg=2.76µs  min=812ns   med=1.83µs  max=8.84ms   p(90)=3.03µs  p(95)=3.76µs   p(99.9)=22.74µs
     http_req_connecting............: avg=555ns   min=0s      med=0s      max=8.59ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.36ms min=7.98ms  med=13.95ms max=276.23ms p(90)=17.84ms p(95)=19.2ms   p(99.9)=27.25ms
       { expected_response:true }...: avg=14.36ms min=7.98ms  med=13.95ms max=276.23ms p(90)=17.84ms p(95)=19.2ms   p(99.9)=27.25ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 411768
     http_req_receiving.............: avg=69.59µs min=25.36µs med=43.54µs max=171.89ms p(90)=91.02µs p(95)=167.32µs p(99.9)=2.02ms 
     http_req_sending...............: avg=29.96µs min=4.31µs  med=7.83µs  max=113.63ms p(90)=16.33µs p(95)=88.8µs   p(99.9)=1.84ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.26ms min=7.9ms   med=13.86ms max=275.9ms  p(90)=17.73ms p(95)=19.09ms  p(99.9)=26.97ms
     http_reqs......................: 411768  3404.405137/s
     iteration_duration.............: avg=14.56ms min=8.21ms  med=14.15ms max=303.57ms p(90)=18.03ms p(95)=19.39ms  p(99.9)=27.48ms
     iterations.....................: 411668  3403.578359/s
     success_rate...................: 100.00% ✓ 411668      ✗ 0     
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

     checks.........................: 100.00% ✓ 1215915     ✗ 0     
     data_received..................: 36 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.4µs   min=791ns   med=1.83µs  max=4.13ms   p(90)=3.02µs  p(95)=3.74µs   p(99.9)=22.76µs
     http_req_connecting............: avg=224ns   min=0s      med=0s      max=4.08ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.6ms  min=8.34ms  med=14.17ms max=273.46ms p(90)=18.05ms p(95)=19.42ms  p(99.9)=27.29ms
       { expected_response:true }...: avg=14.6ms  min=8.34ms  med=14.17ms max=273.46ms p(90)=18.05ms p(95)=19.42ms  p(99.9)=27.29ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405405
     http_req_receiving.............: avg=67.86µs min=23.69µs med=42.87µs max=183.44ms p(90)=89.37µs p(95)=166.86µs p(99.9)=1.71ms 
     http_req_sending...............: avg=30.52µs min=4.26µs  med=7.76µs  max=255.41ms p(90)=15.49µs p(95)=90.58µs  p(99.9)=1.57ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.5ms  min=8.29ms  med=14.07ms max=258.95ms p(90)=17.95ms p(95)=19.31ms  p(99.9)=27.08ms
     http_reqs......................: 405405  3351.349184/s
     iteration_duration.............: avg=14.79ms min=8.53ms  med=14.36ms max=285.48ms p(90)=18.24ms p(95)=19.61ms  p(99.9)=27.52ms
     iterations.....................: 405305  3350.522517/s
     success_rate...................: 100.00% ✓ 405305      ✗ 0     
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

     checks.........................: 100.00% ✓ 1214787     ✗ 0     
     data_received..................: 35 GB   293 MB/s
     data_sent......................: 487 MB  4.0 MB/s
     http_req_blocked...............: avg=2.43µs  min=801ns   med=1.84µs  max=4.01ms   p(90)=3µs     p(95)=3.7µs    p(99.9)=24.14µs
     http_req_connecting............: avg=239ns   min=0s      med=0s      max=3.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.61ms min=8.33ms  med=14.18ms max=281.36ms p(90)=18.12ms p(95)=19.49ms  p(99.9)=27.69ms
       { expected_response:true }...: avg=14.61ms min=8.33ms  med=14.18ms max=281.36ms p(90)=18.12ms p(95)=19.49ms  p(99.9)=27.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 405029
     http_req_receiving.............: avg=66.57µs min=24.29µs med=41.62µs max=163.93ms p(90)=88.02µs p(95)=167.93µs p(99.9)=1.84ms 
     http_req_sending...............: avg=30.55µs min=4.4µs   med=7.8µs   max=163.62ms p(90)=15.64µs p(95)=91.78µs  p(99.9)=1.65ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.51ms min=8.28ms  med=14.09ms max=280.78ms p(90)=18.02ms p(95)=19.38ms  p(99.9)=27.49ms
     http_reqs......................: 405029  3348.353377/s
     iteration_duration.............: avg=14.8ms  min=8.52ms  med=14.37ms max=303.19ms p(90)=18.31ms p(95)=19.68ms  p(99.9)=27.92ms
     iterations.....................: 404929  3347.526682/s
     success_rate...................: 100.00% ✓ 404929      ✗ 0     
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

     checks.........................: 100.00% ✓ 1184823     ✗ 0     
     data_received..................: 35 GB   285 MB/s
     data_sent......................: 475 MB  3.9 MB/s
     http_req_blocked...............: avg=2.96µs  min=902ns   med=2.38µs  max=3.45ms   p(90)=3.88µs  p(95)=4.66µs   p(99.9)=31.96µs
     http_req_connecting............: avg=216ns   min=0s      med=0s      max=3.41ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=14.98ms min=8.72ms  med=14.61ms max=277.59ms p(90)=18.18ms p(95)=19.44ms  p(99.9)=27.81ms
       { expected_response:true }...: avg=14.98ms min=8.72ms  med=14.61ms max=277.59ms p(90)=18.18ms p(95)=19.44ms  p(99.9)=27.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 395041
     http_req_receiving.............: avg=73.81µs min=23.74µs med=46.76µs max=170.14ms p(90)=97.08µs p(95)=181.92µs p(99.9)=1.87ms 
     http_req_sending...............: avg=34.4µs  min=4.32µs  med=8.96µs  max=180.44ms p(90)=18.35µs p(95)=101.83µs p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=14.87ms min=8.67ms  med=14.5ms  max=277.03ms p(90)=18.07ms p(95)=19.32ms  p(99.9)=27.59ms
     http_reqs......................: 395041  3265.826351/s
     iteration_duration.............: avg=15.18ms min=8.86ms  med=14.8ms  max=304.57ms p(90)=18.37ms p(95)=19.64ms  p(99.9)=28.04ms
     iterations.....................: 394941  3264.999646/s
     success_rate...................: 100.00% ✓ 394941      ✗ 0     
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

     checks.........................: 100.00% ✓ 1021053     ✗ 0     
     data_received..................: 30 GB   245 MB/s
     data_sent......................: 409 MB  3.4 MB/s
     http_req_blocked...............: avg=2.5µs   min=782ns   med=1.86µs  max=3.6ms    p(90)=3.22µs  p(95)=4.04µs   p(99.9)=25.51µs
     http_req_connecting............: avg=271ns   min=0s      med=0s      max=3.56ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.41ms min=11.66ms med=16.98ms max=284.08ms p(90)=20.41ms p(95)=21.64ms  p(99.9)=28.86ms
       { expected_response:true }...: avg=17.41ms min=11.66ms med=16.98ms max=284.08ms p(90)=20.41ms p(95)=21.64ms  p(99.9)=28.86ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 340451
     http_req_receiving.............: avg=65.86µs min=23.87µs med=43.77µs max=55.66ms  p(90)=92.06µs p(95)=144.99µs p(99.9)=1.51ms 
     http_req_sending...............: avg=29.54µs min=4.36µs  med=7.94µs  max=193.46ms p(90)=16.83µs p(95)=81.77µs  p(99.9)=1.42ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.32ms min=11.61ms med=16.89ms max=279.88ms p(90)=20.31ms p(95)=21.53ms  p(99.9)=28.6ms 
     http_reqs......................: 340451  2804.525871/s
     iteration_duration.............: avg=17.62ms min=11.81ms med=17.18ms max=292.89ms p(90)=20.6ms  p(95)=21.83ms  p(99.9)=29.07ms
     iterations.....................: 340351  2803.702103/s
     success_rate...................: 100.00% ✓ 340351      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 1018503     ✗ 0     
     data_received..................: 30 GB   245 MB/s
     data_sent......................: 408 MB  3.4 MB/s
     http_req_blocked...............: avg=2.52µs  min=801ns   med=1.88µs  max=4.73ms   p(90)=3.24µs  p(95)=4.01µs   p(99.9)=24.95µs
     http_req_connecting............: avg=254ns   min=0s      med=0s      max=3.87ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.46ms min=11.68ms med=17.03ms max=274.01ms p(90)=20.48ms p(95)=21.73ms  p(99.9)=28.94ms
       { expected_response:true }...: avg=17.46ms min=11.68ms med=17.03ms max=274.01ms p(90)=20.48ms p(95)=21.73ms  p(99.9)=28.94ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 339601
     http_req_receiving.............: avg=66.21µs min=23.56µs med=43.54µs max=143.71ms p(90)=91.71µs p(95)=143.97µs p(99.9)=1.42ms 
     http_req_sending...............: avg=28.51µs min=4.37µs  med=7.97µs  max=193.64ms p(90)=16.82µs p(95)=80.89µs  p(99.9)=1.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.36ms min=11.57ms med=16.94ms max=273.44ms p(90)=20.37ms p(95)=21.62ms  p(99.9)=28.68ms
     http_reqs......................: 339601  2797.34369/s
     iteration_duration.............: avg=17.66ms min=11.9ms  med=17.23ms max=286.82ms p(90)=20.67ms p(95)=21.93ms  p(99.9)=29.19ms
     iterations.....................: 339501  2796.519976/s
     success_rate...................: 100.00% ✓ 339501      ✗ 0     
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

     checks.........................: 100.00% ✓ 999585      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 401 MB  3.3 MB/s
     http_req_blocked...............: avg=2.65µs  min=762ns   med=1.82µs  max=71.73ms  p(90)=3.17µs  p(95)=3.97µs   p(99.9)=24.57µs
     http_req_connecting............: avg=232ns   min=0s      med=0s      max=4.98ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.79ms min=11.74ms med=17.37ms max=290.54ms p(90)=20.87ms p(95)=22.12ms  p(99.9)=29.3ms 
       { expected_response:true }...: avg=17.79ms min=11.74ms med=17.37ms max=290.54ms p(90)=20.87ms p(95)=22.12ms  p(99.9)=29.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 333295
     http_req_receiving.............: avg=63.44µs min=23.18µs med=42.23µs max=40.75ms  p(90)=88.71µs p(95)=140.19µs p(99.9)=1.3ms  
     http_req_sending...............: avg=27.8µs  min=4.2µs   med=7.82µs  max=253.87ms p(90)=16.2µs  p(95)=81.5µs   p(99.9)=1.37ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.7ms  min=11.67ms med=17.28ms max=290.25ms p(90)=20.77ms p(95)=22.01ms  p(99.9)=29.05ms
     http_reqs......................: 333295  2745.463459/s
     iteration_duration.............: avg=17.99ms min=11.98ms med=17.57ms max=301.59ms p(90)=21.06ms p(95)=22.32ms  p(99.9)=29.52ms
     iterations.....................: 333195  2744.639725/s
     success_rate...................: 100.00% ✓ 333195      ✗ 0     
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

     checks.........................: 100.00% ✓ 999090      ✗ 0     
     data_received..................: 29 GB   240 MB/s
     data_sent......................: 400 MB  3.3 MB/s
     http_req_blocked...............: avg=3.03µs  min=851ns   med=2.26µs  max=9.86ms   p(90)=3.66µs  p(95)=4.43µs   p(99.9)=30.62µs
     http_req_connecting............: avg=394ns   min=0s      med=0s      max=9.84ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=17.79ms min=11.86ms med=17.36ms max=287.19ms p(90)=20.86ms p(95)=22.16ms  p(99.9)=29.66ms
       { expected_response:true }...: avg=17.79ms min=11.86ms med=17.36ms max=287.19ms p(90)=20.86ms p(95)=22.16ms  p(99.9)=29.66ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 333130
     http_req_receiving.............: avg=67.95µs min=24.46µs med=45.31µs max=74.73ms  p(90)=92.63µs p(95)=152.58µs p(99.9)=1.38ms 
     http_req_sending...............: avg=29.5µs  min=4.13µs  med=8.53µs  max=183.39ms p(90)=16.75µs p(95)=88.71µs  p(99.9)=1.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=17.7ms  min=11.81ms med=17.27ms max=283.06ms p(90)=20.76ms p(95)=22.04ms  p(99.9)=29.38ms
     http_reqs......................: 333130  2743.893087/s
     iteration_duration.............: avg=18ms    min=12.02ms med=17.56ms max=301.2ms  p(90)=21.07ms p(95)=22.36ms  p(99.9)=30.02ms
     iterations.....................: 333030  2743.069417/s
     success_rate...................: 100.00% ✓ 333030      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 751686      ✗ 0     
     data_received..................: 22 GB   180 MB/s
     data_sent......................: 301 MB  2.5 MB/s
     http_req_blocked...............: avg=3.25µs  min=972ns   med=2.5µs   max=4.08ms   p(90)=4.07µs  p(95)=4.79µs   p(99.9)=35.98µs 
     http_req_connecting............: avg=410ns   min=0s      med=0s      max=4.02ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=23.71ms min=17.03ms med=23.37ms max=306.69ms p(90)=26.72ms p(95)=27.83ms  p(99.9)=33.56ms 
       { expected_response:true }...: avg=23.71ms min=17.03ms med=23.37ms max=306.69ms p(90)=26.72ms p(95)=27.83ms  p(99.9)=33.56ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 250662
     http_req_receiving.............: avg=68.63µs min=25.84µs med=52.71µs max=139.73ms p(90)=94.1µs  p(95)=118.69µs p(99.9)=937.14µs
     http_req_sending...............: avg=28.5µs  min=4.73µs  med=10.22µs max=185.4ms  p(90)=18.08µs p(95)=25.72µs  p(99.9)=942.48µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=23.62ms min=16.97ms med=23.27ms max=306.33ms p(90)=26.61ms p(95)=27.72ms  p(99.9)=33.4ms  
     http_reqs......................: 250662  2056.622349/s
     iteration_duration.............: avg=23.93ms min=17.19ms med=23.58ms max=316.15ms p(90)=26.93ms p(95)=28.04ms  p(99.9)=33.81ms 
     iterations.....................: 250562  2055.801873/s
     success_rate...................: 100.00% ✓ 250562      ✗ 0     
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

     checks.........................: 100.00% ✓ 548379      ✗ 0     
     data_received..................: 16 GB   131 MB/s
     data_sent......................: 220 MB  1.8 MB/s
     http_req_blocked...............: avg=4.14µs  min=1.09µs  med=3.29µs  max=3.52ms   p(90)=5.25µs   p(95)=6.1µs    p(99.9)=40.55µs 
     http_req_connecting............: avg=506ns   min=0s      med=0s      max=3.49ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=32.57ms min=17.76ms med=32.1ms  max=311.96ms p(90)=37.82ms  p(95)=39.84ms  p(99.9)=56.4ms  
       { expected_response:true }...: avg=32.57ms min=17.76ms med=32.1ms  max=311.96ms p(90)=37.82ms  p(95)=39.84ms  p(99.9)=56.4ms  
     http_req_failed................: 0.00%   ✓ 0           ✗ 182893
     http_req_receiving.............: avg=79.3µs  min=25.94µs med=64.4µs  max=164.21ms p(90)=107.57µs p(95)=129.67µs p(99.9)=953.79µs
     http_req_sending...............: avg=28.39µs min=4.84µs  med=13.55µs max=164.61ms p(90)=21.9µs   p(95)=26.86µs  p(99.9)=894.81µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=32.46ms min=17.71ms med=31.99ms max=311.42ms p(90)=37.71ms  p(95)=39.73ms  p(99.9)=55.98ms 
     http_reqs......................: 182893  1499.798799/s
     iteration_duration.............: avg=32.81ms min=19.91ms med=32.33ms max=324.63ms p(90)=38.05ms  p(95)=40.06ms  p(99.9)=56.9ms  
     iterations.....................: 182793  1498.978758/s
     success_rate...................: 100.00% ✓ 182793      ✗ 0     
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

     checks.........................: 100.00% ✓ 527406      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 211 MB  1.7 MB/s
     http_req_blocked...............: avg=3.73µs  min=922ns   med=2.82µs  max=3.8ms    p(90)=5.12µs   p(95)=6.07µs   p(99.9)=42.31µs
     http_req_connecting............: avg=420ns   min=0s      med=0s      max=3.76ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=33.86ms min=16.65ms med=33.59ms max=317.61ms p(90)=39.61ms  p(95)=41.29ms  p(99.9)=49.88ms
       { expected_response:true }...: avg=33.86ms min=16.65ms med=33.59ms max=317.61ms p(90)=39.61ms  p(95)=41.29ms  p(99.9)=49.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 175902
     http_req_receiving.............: avg=86.48µs min=27.01µs med=59.59µs max=158.45ms p(90)=122.52µs p(95)=169.65µs p(99.9)=1.55ms 
     http_req_sending...............: avg=31.03µs min=4.62µs  med=11.08µs max=85.67ms  p(90)=23.82µs  p(95)=69.04µs  p(99.9)=1.46ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=33.74ms min=16.52ms med=33.48ms max=317.14ms p(90)=39.49ms  p(95)=41.16ms  p(99.9)=49.41ms
     http_reqs......................: 175902  1442.511701/s
     iteration_duration.............: avg=34.11ms min=20.26ms med=33.83ms max=324.18ms p(90)=39.83ms  p(95)=41.52ms  p(99.9)=50.14ms
     iterations.....................: 175802  1441.691635/s
     success_rate...................: 100.00% ✓ 175802      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.365.2)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 516405      ✗ 0     
     data_received..................: 15 GB   124 MB/s
     data_sent......................: 207 MB  1.7 MB/s
     http_req_blocked...............: avg=3.94µs  min=912ns   med=2.13µs  max=8.51ms   p(90)=3.61µs  p(95)=4.32µs   p(99.9)=24.21µs 
     http_req_connecting............: avg=1.33µs  min=0s      med=0s      max=8.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.63ms min=17.92ms med=34.06ms max=300.4ms  p(90)=41.35ms p(95)=43.7ms   p(99.9)=55.94ms 
       { expected_response:true }...: avg=34.63ms min=17.92ms med=34.06ms max=300.4ms  p(90)=41.35ms p(95)=43.7ms   p(99.9)=55.94ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 172235
     http_req_receiving.............: avg=75.88µs min=25.36µs med=58.41µs max=208.91ms p(90)=96.9µs  p(95)=114.43µs p(99.9)=740.48µs
     http_req_sending...............: avg=22.39µs min=4.68µs  med=10.06µs max=219.27ms p(90)=16.79µs p(95)=20.65µs  p(99.9)=774.55µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.53ms min=17.81ms med=33.97ms max=285.87ms p(90)=41.25ms p(95)=43.61ms  p(99.9)=55.6ms  
     http_reqs......................: 172235  1412.2702/s
     iteration_duration.............: avg=34.85ms min=20.24ms med=34.26ms max=318.15ms p(90)=41.54ms p(95)=43.89ms  p(99.9)=56.19ms 
     iterations.....................: 172135  1411.450233/s
     success_rate...................: 100.00% ✓ 172135      ✗ 0     
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

     checks.........................: 100.00% ✓ 193863     ✗ 0    
     data_received..................: 5.7 GB  46 MB/s
     data_sent......................: 78 MB   636 kB/s
     http_req_blocked...............: avg=4.57µs  min=1.08µs  med=2.86µs  max=3.89ms   p(90)=4.28µs   p(95)=4.85µs   p(99.9)=51.66µs 
     http_req_connecting............: avg=1.5µs   min=0s      med=0s      max=3.84ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.49ms min=18.73ms med=90.76ms max=317.69ms p(90)=116.76ms p(95)=124.88ms p(99.9)=161.32ms
       { expected_response:true }...: avg=92.49ms min=18.73ms med=90.76ms max=317.69ms p(90)=116.76ms p(95)=124.88ms p(99.9)=161.32ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64721
     http_req_receiving.............: avg=80.68µs min=27.88µs med=71.88µs max=149.66ms p(90)=103.96µs p(95)=115.79µs p(99.9)=496.24µs
     http_req_sending...............: avg=23.82µs min=4.92µs  med=14.41µs max=143.45ms p(90)=20.09µs  p(95)=22.1µs   p(99.9)=471.77µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.39ms min=18.61ms med=90.67ms max=317.59ms p(90)=116.66ms p(95)=124.78ms p(99.9)=160.81ms
     http_reqs......................: 64721   529.672806/s
     iteration_duration.............: avg=92.86ms min=34.39ms med=91.04ms max=327.41ms p(90)=117.02ms p(95)=125.14ms p(99.9)=162.5ms 
     iterations.....................: 64621   528.854412/s
     success_rate...................: 100.00% ✓ 64621      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 190698     ✗ 0    
     data_received..................: 5.6 GB  46 MB/s
     data_sent......................: 77 MB   626 kB/s
     http_req_blocked...............: avg=5.11µs   min=1.31µs  med=3.28µs  max=4.29ms   p(90)=4.81µs   p(95)=5.48µs   p(99.9)=50.02µs 
     http_req_connecting............: avg=1.57µs   min=0s      med=0s      max=4.25ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=93.99ms  min=20.31ms med=91.44ms max=361.2ms  p(90)=114.99ms p(95)=124.6ms  p(99.9)=219.41ms
       { expected_response:true }...: avg=93.99ms  min=20.31ms med=91.44ms max=361.2ms  p(90)=114.99ms p(95)=124.6ms  p(99.9)=219.41ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 63666
     http_req_receiving.............: avg=100.19µs min=30.57µs med=72.38µs max=223.35ms p(90)=104.99µs p(95)=117.28µs p(99.9)=627.1µs 
     http_req_sending...............: avg=22.46µs  min=5.43µs  med=14.55µs max=110.95ms p(90)=20.67µs  p(95)=22.85µs  p(99.9)=586.29µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.87ms  min=20.12ms med=91.34ms max=351.7ms  p(90)=114.87ms p(95)=124.39ms p(99.9)=218.35ms
     http_reqs......................: 63666   520.902144/s
     iteration_duration.............: avg=94.4ms   min=30.67ms med=91.73ms max=372.47ms p(90)=115.28ms p(95)=124.89ms p(99.9)=221.72ms
     iterations.....................: 63566   520.083964/s
     success_rate...................: 100.00% ✓ 63566      ✗ 0    
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

     checks.........................: 100.00% ✓ 151206     ✗ 0    
     data_received..................: 4.4 GB  36 MB/s
     data_sent......................: 61 MB   496 kB/s
     http_req_blocked...............: avg=3.95µs   min=1.07µs  med=2.81µs   max=2.2ms    p(90)=4.15µs   p(95)=4.69µs   p(99.9)=106.43µs
     http_req_connecting............: avg=929ns    min=0s      med=0s       max=2.18ms   p(90)=0s       p(95)=0s       p(99.9)=24µs    
     http_req_duration..............: avg=118.63ms min=21.13ms med=116.96ms max=322.12ms p(90)=146.87ms p(95)=156.45ms p(99.9)=200.22ms
       { expected_response:true }...: avg=118.63ms min=21.13ms med=116.96ms max=322.12ms p(90)=146.87ms p(95)=156.45ms p(99.9)=200.22ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 50502
     http_req_receiving.............: avg=82.06µs  min=28.62µs med=75.3µs   max=113.68ms p(90)=105.37µs p(95)=116.81µs p(99.9)=471.81µs
     http_req_sending...............: avg=20.62µs  min=4.86µs  med=14.95µs  max=96.92ms  p(90)=19.98µs  p(95)=21.83µs  p(99.9)=442.69µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=118.52ms min=21.06ms med=116.86ms max=321.71ms p(90)=146.75ms p(95)=156.32ms p(99.9)=199.94ms
     http_reqs......................: 50502   412.826714/s
     iteration_duration.............: avg=119.08ms min=36.82ms med=117.25ms max=337.11ms p(90)=147.14ms p(95)=156.71ms p(99.9)=203.36ms
     iterations.....................: 50402   412.009267/s
     success_rate...................: 100.00% ✓ 50402      ✗ 0    
     vus............................: 50      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.6)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 97218      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   319 kB/s
     http_req_blocked...............: avg=7.05µs   min=1.48µs  med=3.84µs   max=4.29ms   p(90)=5.43µs   p(95)=6.09µs   p(99.9)=1.34ms  
     http_req_connecting............: avg=2.93µs   min=0s      med=0s       max=4.25ms   p(90)=0s       p(95)=0s       p(99.9)=1.31ms  
     http_req_duration..............: avg=184.48ms min=17.31ms med=170.84ms max=758.04ms p(90)=214.9ms  p(95)=234.67ms p(99.9)=688.81ms
       { expected_response:true }...: avg=184.48ms min=17.31ms med=170.84ms max=758.04ms p(90)=214.9ms  p(95)=234.67ms p(99.9)=688.81ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32506
     http_req_receiving.............: avg=98.45µs  min=35µs    med=89µs     max=102.31ms p(90)=120.01µs p(95)=132.49µs p(99.9)=655.3µs 
     http_req_sending...............: avg=32.4µs   min=6.26µs  med=18.72µs  max=114.22ms p(90)=23.74µs  p(95)=25.76µs  p(99.9)=567.84µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=184.35ms min=17.18ms med=170.73ms max=757.93ms p(90)=214.75ms p(95)=234.53ms p(99.9)=688.68ms
     http_reqs......................: 32506   265.911017/s
     iteration_duration.............: avg=185.31ms min=57.34ms med=171.26ms max=758.31ms p(90)=215.28ms p(95)=235.55ms p(99.9)=689.14ms
     iterations.....................: 32406   265.09298/s
     success_rate...................: 100.00% ✓ 32406      ✗ 0    
     vus............................: 43      min=0        max=50 
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

     checks.........................: 100.00% ✓ 96117      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 39 MB   315 kB/s
     http_req_blocked...............: avg=6.43µs   min=1.41µs  med=3.55µs   max=3.31ms   p(90)=4.93µs   p(95)=5.51µs   p(99.9)=1.22ms  
     http_req_connecting............: avg=2.63µs   min=0s      med=0s       max=3.28ms   p(90)=0s       p(95)=0s       p(99.9)=1.19ms  
     http_req_duration..............: avg=186.56ms min=22.36ms med=187.32ms max=378.09ms p(90)=208.84ms p(95)=213.88ms p(99.9)=278.82ms
       { expected_response:true }...: avg=186.56ms min=22.36ms med=187.32ms max=378.09ms p(90)=208.84ms p(95)=213.88ms p(99.9)=278.82ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32139
     http_req_receiving.............: avg=94.92µs  min=34.4µs  med=86µs     max=120.45ms p(90)=115.94µs p(95)=126.97µs p(99.9)=557.97µs
     http_req_sending...............: avg=31.16µs  min=6.54µs  med=17.13µs  max=88.65ms  p(90)=21.85µs  p(95)=23.6µs   p(99.9)=977.94µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=186.43ms min=22.28ms med=187.2ms  max=377.74ms p(90)=208.71ms p(95)=213.74ms p(99.9)=278.63ms
     http_reqs......................: 32139   262.160495/s
     iteration_duration.............: avg=187.37ms min=48.26ms med=187.75ms max=390.9ms  p(90)=209.1ms  p(95)=214.15ms p(99.9)=281.69ms
     iterations.....................: 32039   261.344786/s
     success_rate...................: 100.00% ✓ 32039      ✗ 0    
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

