## Overview for: `constant-vus-over-time`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario executes a constant load of **50 VUs** over **120s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-nightly-net-11 | 16.8.0-p.20 | 5,550 | 5,569 | 5,542 | 0.2% | 364 MB | 67.2 KB |  |
| fusion-net-11 | 16.7.7 | 5,455 | 5,482 | 5,449 | 0.3% | 363 MB | 68.1 KB |  |
| fusion-fed-net-11 | 16.7.7 | 5,448 | 5,465 | 5,408 | 0.5% | 361 MB | 67.9 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.20 | 5,424 | 5,447 | 5,397 | 0.3% | 374 MB | 70.5 KB |  |
| fusion-fed-aot-11 | 16.7.7 | 5,366 | 5,387 | 5,345 | 0.3% | 120 MB | 22.9 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.20 | 5,321 | 5,363 | 5,312 | 0.4% | 116 MB | 22.4 KB |  |
| fusion-aot-11 | 16.7.7 | 5,302 | 5,334 | 5,274 | 0.4% | 119 MB | 23.0 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.20 | 5,247 | 5,265 | 5,230 | 0.3% | 120 MB | 23.3 KB |  |
| feddi-gateway | 2026-11-03-0517 | 5,022 | 5,048 | 4,974 | 0.6% | 2,289 MB | 466.7 KB |  |
| hive-router | v0.3.17 | 4,710 | 4,723 | 4,622 | 0.9% | 101 MB | 22.0 KB |  |
| hive-router-nightly | v0.3.19-nightly.e7e70652 | 4,628 | 4,679 | 4,615 | 0.5% | 93 MB | 20.6 KB |  |
| grafbase | 0.53.5 | 1,855 | 1,859 | 1,850 | 0.2% | 113 MB | 62.1 KB |  |
| caliban | 3.2.1 | 1,587 | 1,588 | 1,587 | 0.0% | 7,091 MB | 4,575.5 KB |  |
| cosmo | 0.373.0 | 1,442 | 1,445 | 1,438 | 0.2% | 166 MB | 118.0 KB |  |
| hive-gateway-router-runtime | 2.15.10 | 607 | 609 | 606 | 0.2% | 2,594 MB | 4,375.8 KB |  |
| apollo-router | v2.19.1 | 536 | 536 | 535 | 0.1% | 173 MB | 331.1 KB |  |
| apollo-router-nightly | v3.0.0-preview.0-nightly.fbceee06 | 475 | 476 | 475 | 0.1% | 196 MB | 422.9 KB |  |
| apollo-router-v3 | v3.0.0-preview.0 | 403 | 405 | 403 | 0.2% | 198 MB | 503.8 KB |  |
| hive-gateway | 2.15.10 | 297 | 298 | 296 | 0.3% | 3,269 MB | 11,269.2 KB |  |
| apollo-gateway | 2.14.4 | 272 | 273 | 271 | 0.4% | 2,155 MB | 8,111.9 KB |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1999587     ✗ 0     
     data_received..................: 58 GB   486 MB/s
     data_sent......................: 801 MB  6.7 MB/s
     http_req_blocked...............: avg=2.51µs  min=782ns    med=1.95µs  max=6.73ms   p(90)=3.11µs  p(95)=3.74µs   p(99.9)=27.28µs
     http_req_connecting............: avg=135ns   min=0s       med=0s      max=3.96ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.79ms  min=789.28µs med=7.86ms  max=266.47ms p(90)=14.15ms p(95)=17.34ms  p(99.9)=29.93ms
       { expected_response:true }...: avg=8.79ms  min=789.28µs med=7.86ms  max=266.47ms p(90)=14.15ms p(95)=17.34ms  p(99.9)=29.93ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 666629
     http_req_receiving.............: avg=92.54µs min=23.49µs  med=45.24µs max=97.97ms  p(90)=85.58µs p(95)=185.21µs p(99.9)=6.29ms 
     http_req_sending...............: avg=41.37µs min=4.3µs    med=8.05µs  max=168.24ms p(90)=13.51µs p(95)=97.32µs  p(99.9)=4.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.66ms  min=720.62µs med=7.76ms  max=266.04ms p(90)=13.92ms p(95)=17.06ms  p(99.9)=29.37ms
     http_reqs......................: 666629  5550.507211/s
     iteration_duration.............: avg=8.99ms  min=1ms      med=8.05ms  max=274.73ms p(90)=14.36ms p(95)=17.56ms  p(99.9)=30.21ms
     iterations.....................: 666529  5549.674587/s
     success_rate...................: 100.00% ✓ 666529      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1965441     ✗ 0     
     data_received..................: 57 GB   477 MB/s
     data_sent......................: 788 MB  6.6 MB/s
     http_req_blocked...............: avg=2.9µs   min=922ns    med=2.38µs max=6.48ms   p(90)=3.55µs  p(95)=4.16µs   p(99.9)=32.85µs
     http_req_connecting............: avg=136ns   min=0s       med=0s     max=3.49ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.95ms  min=782.1µs  med=7.98ms max=279.29ms p(90)=14.54ms p(95)=17.88ms  p(99.9)=31.02ms
       { expected_response:true }...: avg=8.95ms  min=782.1µs  med=7.98ms max=279.29ms p(90)=14.54ms p(95)=17.88ms  p(99.9)=31.02ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 655247
     http_req_receiving.............: avg=95.33µs min=25.07µs  med=46.8µs max=150.39ms p(90)=88.55µs p(95)=193.41µs p(99.9)=6.21ms 
     http_req_sending...............: avg=43.24µs min=4.53µs   med=8.57µs max=103.78ms p(90)=14.19µs p(95)=101.69µs p(99.9)=5.05ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s     max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.81ms  min=730.97µs med=7.88ms max=278.61ms p(90)=14.29ms p(95)=17.61ms  p(99.9)=30.52ms
     http_reqs......................: 655247  5455.432682/s
     iteration_duration.............: avg=9.14ms  min=983.71µs med=8.17ms max=290.08ms p(90)=14.75ms p(95)=18.11ms  p(99.9)=31.29ms
     iterations.....................: 655147  5454.600105/s
     success_rate...................: 100.00% ✓ 655147      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-net-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1962870     ✗ 0     
     data_received..................: 57 GB   477 MB/s
     data_sent......................: 787 MB  6.5 MB/s
     http_req_blocked...............: avg=2.42µs  min=781ns    med=1.86µs  max=4.99ms   p(90)=2.99µs  p(95)=3.61µs   p(99.9)=27.21µs
     http_req_connecting............: avg=135ns   min=0s       med=0s      max=3.17ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=8.96ms  min=795.65µs med=8.06ms  max=268.2ms  p(90)=14.31ms p(95)=17.4ms   p(99.9)=29.77ms
       { expected_response:true }...: avg=8.96ms  min=795.65µs med=8.06ms  max=268.2ms  p(90)=14.31ms p(95)=17.4ms   p(99.9)=29.77ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 654390
     http_req_receiving.............: avg=92.03µs min=22.85µs  med=45.38µs max=107.93ms p(90)=85.9µs  p(95)=188.36µs p(99.9)=6.29ms 
     http_req_sending...............: avg=41.09µs min=3.99µs   med=7.94µs  max=129.78ms p(90)=13.61µs p(95)=98.64µs  p(99.9)=4.69ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.83ms  min=744.37µs med=7.95ms  max=267.71ms p(90)=14.07ms p(95)=17.13ms  p(99.9)=29.32ms
     http_reqs......................: 654390  5448.205478/s
     iteration_duration.............: avg=9.16ms  min=968.16µs med=8.24ms  max=283.51ms p(90)=14.51ms p(95)=17.62ms  p(99.9)=30.05ms
     iterations.....................: 654290  5447.372916/s
     success_rate...................: 100.00% ✓ 654290      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1954284     ✗ 0     
     data_received..................: 57 GB   475 MB/s
     data_sent......................: 783 MB  6.5 MB/s
     http_req_blocked...............: avg=2.49µs  min=781ns    med=1.95µs  max=6.91ms   p(90)=3µs     p(95)=3.61µs   p(99.9)=28.23µs
     http_req_connecting............: avg=139ns   min=0s       med=0s      max=3.92ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9ms     min=796.17µs med=8.08ms  max=266.49ms p(90)=14.37ms p(95)=17.51ms  p(99.9)=30.32ms
       { expected_response:true }...: avg=9ms     min=796.17µs med=8.08ms  max=266.49ms p(90)=14.37ms p(95)=17.51ms  p(99.9)=30.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 651528
     http_req_receiving.............: avg=93.18µs min=25.15µs  med=47.37µs max=174.02ms p(90)=86.12µs p(95)=186.93µs p(99.9)=6.01ms 
     http_req_sending...............: avg=43.1µs  min=4.19µs   med=8.2µs   max=192.88ms p(90)=13.58µs p(95)=97.4µs   p(99.9)=4.94ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.86ms  min=726.68µs med=7.97ms  max=265.89ms p(90)=14.14ms p(95)=17.25ms  p(99.9)=29.93ms
     http_reqs......................: 651528  5424.615221/s
     iteration_duration.............: avg=9.2ms   min=1.14ms   med=8.27ms  max=279.35ms p(90)=14.58ms p(95)=17.74ms  p(99.9)=30.6ms 
     iterations.....................: 651428  5423.782622/s
     success_rate...................: 100.00% ✓ 651428      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-fed-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1933329     ✗ 0     
     data_received..................: 56 GB   470 MB/s
     data_sent......................: 775 MB  6.4 MB/s
     http_req_blocked...............: avg=2.52µs  min=782ns    med=1.98µs  max=7.13ms   p(90)=3.07µs  p(95)=3.66µs   p(99.9)=27.49µs
     http_req_connecting............: avg=144ns   min=0s       med=0s      max=4.06ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.1ms   min=836.28µs med=8.21ms  max=282.27ms p(90)=14.49ms p(95)=17.6ms   p(99.9)=29.79ms
       { expected_response:true }...: avg=9.1ms   min=836.28µs med=8.21ms  max=282.27ms p(90)=14.49ms p(95)=17.6ms   p(99.9)=29.79ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 644543
     http_req_receiving.............: avg=91.97µs min=24.48µs  med=45.17µs max=196.3ms  p(90)=85.23µs p(95)=188.65µs p(99.9)=6.11ms 
     http_req_sending...............: avg=41.32µs min=4.48µs   med=8.29µs  max=126.61ms p(90)=13.83µs p(95)=99.11µs  p(99.9)=4.67ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=8.97ms  min=776.48µs med=8.1ms   max=281.59ms p(90)=14.26ms p(95)=17.32ms  p(99.9)=29.31ms
     http_reqs......................: 644543  5366.137304/s
     iteration_duration.............: avg=9.3ms   min=1.25ms   med=8.39ms  max=293.33ms p(90)=14.7ms  p(95)=17.82ms  p(99.9)=30.1ms 
     iterations.....................: 644443  5365.304755/s
     success_rate...................: 100.00% ✓ 644443      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-aot-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1917063     ✗ 0     
     data_received..................: 56 GB   466 MB/s
     data_sent......................: 768 MB  6.4 MB/s
     http_req_blocked...............: avg=2.41µs  min=801ns    med=1.88µs  max=6.28ms   p(90)=3.03µs  p(95)=3.63µs   p(99.9)=27.83µs
     http_req_connecting............: avg=141ns   min=0s       med=0s      max=3.37ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.18ms  min=836.37µs med=8.28ms  max=267.12ms p(90)=14.68ms p(95)=17.79ms  p(99.9)=30.37ms
       { expected_response:true }...: avg=9.18ms  min=836.37µs med=8.28ms  max=267.12ms p(90)=14.68ms p(95)=17.79ms  p(99.9)=30.37ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 639121
     http_req_receiving.............: avg=92.05µs min=25.58µs  med=45.91µs max=122.33ms p(90)=88.87µs p(95)=196.38µs p(99.9)=5.65ms 
     http_req_sending...............: avg=41.38µs min=4.39µs   med=7.97µs  max=131.66ms p(90)=13.76µs p(95)=101.4µs  p(99.9)=4.73ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.05ms  min=760.16µs med=8.18ms  max=266.35ms p(90)=14.47ms p(95)=17.54ms  p(99.9)=29.93ms
     http_reqs......................: 639121  5321.239649/s
     iteration_duration.............: avg=9.38ms  min=1.07ms   med=8.47ms  max=284.58ms p(90)=14.89ms p(95)=18.01ms  p(99.9)=30.64ms
     iterations.....................: 639021  5320.407062/s
     success_rate...................: 100.00% ✓ 639021      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-aot-11 (HotChocolate subgraphs) (16.7.7)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1910403     ✗ 0     
     data_received..................: 56 GB   464 MB/s
     data_sent......................: 766 MB  6.4 MB/s
     http_req_blocked...............: avg=2.95µs  min=922ns    med=2.37µs  max=6.87ms   p(90)=3.63µs  p(95)=4.27µs   p(99.9)=31.98µs
     http_req_connecting............: avg=144ns   min=0s       med=0s      max=4.05ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.21ms  min=852.97µs med=8.23ms  max=252.04ms p(90)=14.92ms p(95)=18.3ms   p(99.9)=31.16ms
       { expected_response:true }...: avg=9.21ms  min=852.97µs med=8.23ms  max=252.04ms p(90)=14.92ms p(95)=18.3ms   p(99.9)=31.16ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 636901
     http_req_receiving.............: avg=97.53µs min=24.95µs  med=46.65µs max=149.19ms p(90)=90.17µs p(95)=203.51µs p(99.9)=6.35ms 
     http_req_sending...............: avg=43.43µs min=4.38µs   med=8.7µs   max=106.34ms p(90)=14.66µs p(95)=106.19µs p(99.9)=4.95ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.07ms  min=778.68µs med=8.12ms  max=251.35ms p(90)=14.69ms p(95)=18.03ms  p(99.9)=30.67ms
     http_reqs......................: 636901  5302.766703/s
     iteration_duration.............: avg=9.41ms  min=1.18ms   med=8.42ms  max=279.52ms p(90)=15.14ms p(95)=18.53ms  p(99.9)=31.42ms
     iterations.....................: 636801  5301.934114/s
     success_rate...................: 100.00% ✓ 636801      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-aot-11 (HotChocolate subgraphs) (16.8.0-p.20)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1890666     ✗ 0     
     data_received..................: 55 GB   459 MB/s
     data_sent......................: 758 MB  6.3 MB/s
     http_req_blocked...............: avg=2.66µs  min=801ns    med=2.05µs  max=62.37ms  p(90)=3.25µs  p(95)=3.88µs   p(99.9)=27.45µs
     http_req_connecting............: avg=241ns   min=0s       med=0s      max=62.32ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.31ms  min=843.28µs med=8.42ms  max=273.27ms p(90)=14.87ms p(95)=17.94ms  p(99.9)=30.19ms
       { expected_response:true }...: avg=9.31ms  min=843.28µs med=8.42ms  max=273.27ms p(90)=14.87ms p(95)=17.94ms  p(99.9)=30.19ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 630322
     http_req_receiving.............: avg=91.8µs  min=24.87µs  med=46.68µs max=121.68ms p(90)=87.66µs p(95)=194.52µs p(99.9)=5.61ms 
     http_req_sending...............: avg=41.43µs min=4.36µs   med=8.28µs  max=124.11ms p(90)=14.16µs p(95)=100.97µs p(99.9)=4.53ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.18ms  min=779.04µs med=8.31ms  max=272.62ms p(90)=14.65ms p(95)=17.7ms   p(99.9)=29.81ms
     http_reqs......................: 630322  5247.845894/s
     iteration_duration.............: avg=9.51ms  min=1.26ms   med=8.61ms  max=285.18ms p(90)=15.07ms p(95)=18.15ms  p(99.9)=30.45ms
     iterations.....................: 630222  5247.013328/s
     success_rate...................: 100.00% ✓ 630222      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (2026-11-03-0517)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1809294     ✗ 0     
     data_received..................: 53 GB   439 MB/s
     data_sent......................: 725 MB  6.0 MB/s
     http_req_blocked...............: avg=3.49µs  min=801ns    med=1.95µs  max=102.29ms p(90)=3.09µs  p(95)=3.68µs   p(99.9)=27.43µs
     http_req_connecting............: avg=1.07µs  min=0s       med=0s      max=102.23ms p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=9.74ms  min=686.55µs med=9.1ms   max=257.14ms p(90)=14.63ms p(95)=17.98ms  p(99.9)=28.51ms
       { expected_response:true }...: avg=9.74ms  min=686.55µs med=9.1ms   max=257.14ms p(90)=14.63ms p(95)=17.98ms  p(99.9)=28.51ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 603198
     http_req_receiving.............: avg=90.6µs  min=23.14µs  med=45.81µs max=42.61ms  p(90)=86.43µs p(95)=191.53µs p(99.9)=6.14ms 
     http_req_sending...............: avg=43.32µs min=4.5µs    med=8.3µs   max=166.07ms p(90)=14.44µs p(95)=102.85µs p(99.9)=4.44ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=9.61ms  min=636.8µs  med=9.01ms  max=173.56ms p(90)=14.37ms p(95)=17.72ms  p(99.9)=28.1ms 
     http_reqs......................: 603198  5022.605425/s
     iteration_duration.............: avg=9.93ms  min=1.05ms   med=9.27ms  max=275.56ms p(90)=14.84ms p(95)=18.19ms  p(99.9)=28.83ms
     iterations.....................: 603098  5021.772762/s
     success_rate...................: 100.00% ✓ 603098      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router (HotChocolate subgraphs) (v0.3.17)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1697208     ✗ 0     
     data_received..................: 50 GB   412 MB/s
     data_sent......................: 680 MB  5.7 MB/s
     http_req_blocked...............: avg=3.1µs   min=801ns    med=2.05µs  max=87.06ms  p(90)=3.31µs  p(95)=3.97µs   p(99.9)=28.83µs
     http_req_connecting............: avg=639ns   min=0s       med=0s      max=87.02ms  p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.4ms  min=944.98µs med=9.75ms  max=263.71ms p(90)=14.67ms p(95)=17.86ms  p(99.9)=28.6ms 
       { expected_response:true }...: avg=10.4ms  min=944.98µs med=9.75ms  max=263.71ms p(90)=14.67ms p(95)=17.86ms  p(99.9)=28.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 565836
     http_req_receiving.............: avg=91.34µs min=24.1µs   med=47.77µs max=85.51ms  p(90)=93.82µs p(95)=202.06µs p(99.9)=5.71ms 
     http_req_sending...............: avg=43.79µs min=4.47µs   med=8.64µs  max=85.79ms  p(90)=15.12µs p(95)=107.17µs p(99.9)=4.47ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.26ms min=871.38µs med=9.66ms  max=263.56ms p(90)=14.42ms p(95)=17.58ms  p(99.9)=28.18ms
     http_reqs......................: 565836  4710.503486/s
     iteration_duration.............: avg=10.59ms min=1.66ms   med=9.94ms  max=281.89ms p(90)=14.88ms p(95)=18.08ms  p(99.9)=28.84ms
     iterations.....................: 565736  4709.671/s
     success_rate...................: 100.00% ✓ 565736      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-router-nightly (HotChocolate subgraphs) (v0.3.19-nightly.e7e70652)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1667784     ✗ 0     
     data_received..................: 49 GB   405 MB/s
     data_sent......................: 668 MB  5.6 MB/s
     http_req_blocked...............: avg=2.65µs  min=841ns    med=2.04µs  max=8.83ms   p(90)=3.22µs  p(95)=3.84µs   p(99.9)=28.76µs
     http_req_connecting............: avg=169ns   min=0s       med=0s      max=4.01ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=10.58ms min=943.38µs med=10.02ms max=282.15ms p(90)=14.68ms p(95)=17.7ms   p(99.9)=28.55ms
       { expected_response:true }...: avg=10.58ms min=943.38µs med=10.02ms max=282.15ms p(90)=14.68ms p(95)=17.7ms   p(99.9)=28.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 556028
     http_req_receiving.............: avg=92.4µs  min=23.38µs  med=48.79µs max=102.76ms p(90)=93.91µs p(95)=202.94µs p(99.9)=5.58ms 
     http_req_sending...............: avg=40.77µs min=4.54µs   med=8.57µs  max=99ms     p(90)=14.93µs p(95)=107.12µs p(99.9)=4.11ms 
     http_req_tls_handshaking.......: avg=0s      min=0s       med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=10.45ms min=865.63µs med=9.93ms  max=281.85ms p(90)=14.44ms p(95)=17.42ms  p(99.9)=28.16ms
     http_reqs......................: 556028  4628.683683/s
     iteration_duration.............: avg=10.78ms min=1.54ms   med=10.21ms max=311.36ms p(90)=14.89ms p(95)=17.92ms  p(99.9)=28.87ms
     iterations.....................: 555928  4627.851228/s
     success_rate...................: 100.00% ✓ 555928      ✗ 0     
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

     checks.........................: 100.00% ✓ 669000      ✗ 0     
     data_received..................: 20 GB   163 MB/s
     data_sent......................: 268 MB  2.2 MB/s
     http_req_blocked...............: avg=4.18µs  min=1.04µs med=2.98µs  max=6.53ms   p(90)=5.06µs   p(95)=6.1µs    p(99.9)=43.23µs
     http_req_connecting............: avg=721ns   min=0s     med=0s      max=6.43ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.64ms min=1.84ms med=26.08ms max=297.53ms p(90)=34.59ms  p(95)=37.43ms  p(99.9)=52.44ms
       { expected_response:true }...: avg=26.64ms min=1.84ms med=26.08ms max=297.53ms p(90)=34.59ms  p(95)=37.43ms  p(99.9)=52.44ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 223100
     http_req_receiving.............: avg=91.8µs  min=28.2µs med=62.45µs max=53.09ms  p(90)=126.43µs p(95)=215.29µs p(99.9)=1.72ms 
     http_req_sending...............: avg=36.78µs min=5µs    med=11.61µs max=78.77ms  p(90)=24.12µs  p(95)=116.53µs p(99.9)=1.75ms 
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.52ms min=1.78ms med=25.95ms max=279.81ms p(90)=34.46ms  p(95)=37.29ms  p(99.9)=52.07ms
     http_reqs......................: 223100  1855.230142/s
     iteration_duration.............: avg=26.89ms min=4.66ms med=26.31ms max=310.78ms p(90)=34.83ms  p(95)=37.65ms  p(99.9)=52.79ms
     iterations.....................: 223000  1854.398573/s
     success_rate...................: 100.00% ✓ 223000      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: caliban (HotChocolate subgraphs) (3.2.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 572412      ✗ 0     
     data_received..................: 17 GB   139 MB/s
     data_sent......................: 229 MB  1.9 MB/s
     http_req_blocked...............: avg=3.91µs   min=852ns   med=2.44µs  max=7.7ms    p(90)=4.2µs    p(95)=4.96µs   p(99.9)=36.03µs 
     http_req_connecting............: avg=1.09µs   min=0s      med=0s      max=7.67ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=31.2ms   min=1.92ms  med=30.32ms max=294.56ms p(90)=44.07ms  p(95)=48.61ms  p(99.9)=73.65ms 
       { expected_response:true }...: avg=31.2ms   min=1.92ms  med=30.32ms max=294.56ms p(90)=44.07ms  p(95)=48.61ms  p(99.9)=73.65ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 190904
     http_req_receiving.............: avg=101.39µs min=26.61µs med=61.47µs max=257.39ms p(90)=101.15µs p(95)=119.25µs p(99.9)=906.87µs
     http_req_sending...............: avg=22.65µs  min=4.68µs  med=11.66µs max=41.21ms  p(90)=19.25µs  p(95)=23.08µs  p(99.9)=815.77µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=31.07ms  min=1.87ms  med=30.22ms max=167.78ms p(90)=43.95ms  p(95)=48.48ms  p(99.9)=72.07ms 
     http_reqs......................: 190904  1587.494847/s
     iteration_duration.............: avg=31.43ms  min=5.03ms  med=30.54ms max=307.46ms p(90)=44.29ms  p(95)=48.82ms  p(99.9)=74.39ms 
     iterations.....................: 190804  1586.66328/s
     success_rate...................: 100.00% ✓ 190804      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: cosmo (HotChocolate subgraphs) (0.373.0)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 520143      ✗ 0     
     data_received..................: 15 GB   126 MB/s
     data_sent......................: 208 MB  1.7 MB/s
     http_req_blocked...............: avg=3.58µs  min=931ns   med=2.04µs  max=7.48ms   p(90)=3.47µs  p(95)=4.14µs   p(99.9)=27.49µs 
     http_req_connecting............: avg=1.21µs  min=0s      med=0s      max=7.45ms   p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=34.38ms min=1.98ms  med=33.48ms max=270.79ms p(90)=49.89ms p(95)=55.03ms  p(99.9)=78.89ms 
       { expected_response:true }...: avg=34.38ms min=1.98ms  med=33.48ms max=270.79ms p(90)=49.89ms p(95)=55.03ms  p(99.9)=78.89ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 173481
     http_req_receiving.............: avg=71µs    min=26.81µs med=59.41µs max=158.72ms p(90)=95.15µs p(95)=111.11µs p(99.9)=674.39µs
     http_req_sending...............: avg=20.75µs min=4.51µs  med=9.63µs  max=175.49ms p(90)=15.44µs p(95)=19.01µs  p(99.9)=733.28µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=34.29ms min=1.93ms  med=33.4ms  max=260.35ms p(90)=49.79ms p(95)=54.94ms  p(99.9)=78.72ms 
     http_reqs......................: 173481  1442.450916/s
     iteration_duration.............: avg=34.6ms  min=3.96ms  med=33.69ms max=288.53ms p(90)=50.08ms p(95)=55.22ms  p(99.9)=79.67ms 
     iterations.....................: 173381  1441.619441/s
     success_rate...................: 100.00% ✓ 173381      ✗ 0     
     vus............................: 50      min=50        max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway-router-runtime (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 219228     ✗ 0    
     data_received..................: 6.4 GB  53 MB/s
     data_sent......................: 88 MB   729 kB/s
     http_req_blocked...............: avg=6.96µs  min=1.13µs  med=2.91µs  max=8.44ms   p(90)=4.33µs   p(95)=4.93µs   p(99.9)=41.17µs 
     http_req_connecting............: avg=3.56µs  min=0s      med=0s      max=8.42ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=81.78ms min=3.44ms  med=79.02ms max=318.48ms p(90)=99.21ms  p(95)=109.53ms p(99.9)=205.77ms
       { expected_response:true }...: avg=81.78ms min=3.44ms  med=79.02ms max=318.48ms p(90)=99.21ms  p(95)=109.53ms p(99.9)=205.77ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 73176
     http_req_receiving.............: avg=77.52µs min=28.14µs med=67.38µs max=82.38ms  p(90)=100.78µs p(95)=113.28µs p(99.9)=615.88µs
     http_req_sending...............: avg=19.05µs min=5.13µs  med=13.2µs  max=82.02ms  p(90)=19.25µs  p(95)=21.36µs  p(99.9)=639.69µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=81.69ms min=3.39ms  med=78.93ms max=317.68ms p(90)=99.12ms  p(95)=109.41ms p(99.9)=205.69ms
     http_reqs......................: 73176   607.263625/s
     iteration_duration.............: avg=82.12ms min=21.2ms  med=79.25ms max=333.53ms p(90)=99.45ms  p(95)=109.79ms p(99.9)=207.6ms 
     iterations.....................: 73076   606.433757/s
     success_rate...................: 100.00% ✓ 73076      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router (HotChocolate subgraphs) (v2.19.1)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 193608     ✗ 0    
     data_received..................: 5.7 GB  47 MB/s
     data_sent......................: 78 MB   644 kB/s
     http_req_blocked...............: avg=7.03µs  min=1.06µs  med=2.77µs  max=8.87ms   p(90)=4.21µs   p(95)=4.78µs   p(99.9)=42.28µs 
     http_req_connecting............: avg=3.98µs  min=0s      med=0s      max=7.97ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=92.6ms  min=4.3ms   med=90.67ms max=302.99ms p(90)=125.09ms p(95)=134.99ms p(99.9)=178.01ms
       { expected_response:true }...: avg=92.6ms  min=4.3ms   med=90.67ms max=302.99ms p(90)=125.09ms p(95)=134.99ms p(99.9)=178.01ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 64636
     http_req_receiving.............: avg=110.4µs min=28.81µs med=71.54µs max=169.36ms p(90)=102.66µs p(95)=115.14µs p(99.9)=632.72µs
     http_req_sending...............: avg=23.64µs min=4.91µs  med=13.66µs max=128.21ms p(90)=19.16µs  p(95)=21.07µs  p(99.9)=638.6µs 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=92.46ms min=4.22ms  med=90.57ms max=217.2ms  p(90)=124.99ms p(95)=134.74ms p(99.9)=174.21ms
     http_reqs......................: 64636   536.179107/s
     iteration_duration.............: avg=92.98ms min=15.45ms med=90.94ms max=318.32ms p(90)=125.35ms p(95)=135.24ms p(99.9)=179.51ms
     iterations.....................: 64536   535.349571/s
     success_rate...................: 100.00% ✓ 64536      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: apollo-router-nightly (HotChocolate subgraphs) (v3.0.0-preview.0-nightly.fbceee06)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 171705     ✗ 0    
     data_received..................: 5.0 GB  42 MB/s
     data_sent......................: 69 MB   571 kB/s
     http_req_blocked...............: avg=7.8µs    min=1.05µs  med=2.46µs   max=9.49ms   p(90)=3.83µs   p(95)=4.37µs   p(99.9)=54.27µs 
     http_req_connecting............: avg=4.97µs   min=0s      med=0s       max=9.44ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=104.45ms min=4.68ms  med=102.39ms max=288.66ms p(90)=138.45ms p(95)=149.97ms p(99.9)=198.86ms
       { expected_response:true }...: avg=104.45ms min=4.68ms  med=102.39ms max=288.66ms p(90)=138.45ms p(95)=149.97ms p(99.9)=198.86ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 57335
     http_req_receiving.............: avg=73.33µs  min=26.88µs med=66.2µs   max=80.38ms  p(90)=97.08µs  p(95)=109.52µs p(99.9)=477.96µs
     http_req_sending...............: avg=20.02µs  min=4.58µs  med=12.5µs   max=99.68ms  p(90)=18.28µs  p(95)=20.02µs  p(99.9)=550.57µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=104.36ms min=4.53ms  med=102.3ms  max=288.53ms p(90)=138.37ms p(95)=149.86ms p(99.9)=198.56ms
     http_reqs......................: 57335   475.338996/s
     iteration_duration.............: avg=104.86ms min=20.8ms  med=102.65ms max=305.8ms  p(90)=138.74ms p(95)=150.27ms p(99.9)=200.44ms
     iterations.....................: 57235   474.509941/s
     success_rate...................: 100.00% ✓ 57235      ✗ 0    
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

     checks.........................: 100.00% ✓ 145677     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 58 MB   484 kB/s
     http_req_blocked...............: avg=4.81µs  min=1.11µs  med=2.74µs   max=4.08ms   p(90)=4.07µs   p(95)=4.59µs   p(99.9)=261.7µs 
     http_req_connecting............: avg=1.84µs  min=0s      med=0s       max=4.04ms   p(90)=0s       p(95)=0s       p(99.9)=183.17µs
     http_req_duration..............: avg=123.1ms min=5.32ms  med=120.73ms max=345.24ms p(90)=160.98ms p(95)=173.51ms p(99.9)=224.83ms
       { expected_response:true }...: avg=123.1ms min=5.32ms  med=120.73ms max=345.24ms p(90)=160.98ms p(95)=173.51ms p(99.9)=224.83ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 48659
     http_req_receiving.............: avg=76.62µs min=28.97µs med=72.71µs  max=25.08ms  p(90)=102.45µs p(95)=114.22µs p(99.9)=473.18µs
     http_req_sending...............: avg=20.62µs min=5.21µs  med=14.53µs  max=65.06ms  p(90)=19.14µs  p(95)=20.8µs   p(99.9)=478.63µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=123ms   min=5.23ms  med=120.64ms max=344.7ms  p(90)=160.9ms  p(95)=173.41ms p(99.9)=224.77ms
     http_reqs......................: 48659   403.185353/s
     iteration_duration.............: avg=123.6ms min=19.22ms med=121.05ms max=363.4ms  p(90)=161.26ms p(95)=173.84ms p(99.9)=228.18ms
     iterations.....................: 48559   402.35676/s
     success_rate...................: 100.00% ✓ 48559      ✗ 0    
     vus............................: 50      min=50       max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: hive-gateway (HotChocolate subgraphs) (2.15.10)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 107568     ✗ 0    
     data_received..................: 3.1 GB  26 MB/s
     data_sent......................: 43 MB   358 kB/s
     http_req_blocked...............: avg=6.69µs   min=1.38µs  med=3.53µs   max=4.41ms   p(90)=4.93µs   p(95)=5.55µs   p(99.9)=1.36ms  
     http_req_connecting............: avg=2.93µs   min=0s      med=0s       max=4.37ms   p(90)=0s       p(95)=0s       p(99.9)=1.26ms  
     http_req_duration..............: avg=166.67ms min=5.28ms  med=149.02ms max=754.79ms p(90)=194.78ms p(95)=220.66ms p(99.9)=696.95ms
       { expected_response:true }...: avg=166.67ms min=5.28ms  med=149.02ms max=754.79ms p(90)=194.78ms p(95)=220.66ms p(99.9)=696.95ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 35956
     http_req_receiving.............: avg=90.48µs  min=34.07µs med=85.96µs  max=44.6ms   p(90)=115.57µs p(95)=126.8µs  p(99.9)=596.87µs
     http_req_sending...............: avg=26.26µs  min=5.85µs  med=17.17µs  max=95.5ms   p(90)=21.71µs  p(95)=23.52µs  p(99.9)=537.46µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=166.55ms min=5.14ms  med=148.9ms  max=754.69ms p(90)=194.68ms p(95)=220.56ms p(99.9)=696.87ms
     http_reqs......................: 35956   297.83222/s
     iteration_duration.............: avg=167.41ms min=18.14ms med=149.34ms max=755.02ms p(90)=195.22ms p(95)=221.22ms p(99.9)=697.21ms
     iterations.....................: 35856   297.003896/s
     success_rate...................: 100.00% ✓ 35856      ✗ 0    
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

     checks.........................: 100.00% ✓ 98427      ✗ 0    
     data_received..................: 2.9 GB  24 MB/s
     data_sent......................: 40 MB   327 kB/s
     http_req_blocked...............: avg=5.88µs   min=1.15µs  med=2.9µs    max=4.15ms   p(90)=4.14µs   p(95)=4.63µs   p(99.9)=1.3ms   
     http_req_connecting............: avg=2.81µs   min=0s      med=0s       max=4.11ms   p(90)=0s       p(95)=0s       p(99.9)=1.28ms  
     http_req_duration..............: avg=182.17ms min=7.45ms  med=169.06ms max=399.46ms p(90)=235.11ms p(95)=240.88ms p(99.9)=310.08ms
       { expected_response:true }...: avg=182.17ms min=7.45ms  med=169.06ms max=399.46ms p(90)=235.11ms p(95)=240.88ms p(99.9)=310.08ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 32909
     http_req_receiving.............: avg=85.07µs  min=30.71µs med=80.59µs  max=37.01ms  p(90)=109.32µs p(95)=119.75µs p(99.9)=384.72µs
     http_req_sending...............: avg=28.94µs  min=5.09µs  med=15.13µs  max=86.85ms  p(90)=18.86µs  p(95)=20.46µs  p(99.9)=526.41µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=182.06ms min=7.35ms  med=168.95ms max=398.91ms p(90)=235.02ms p(95)=240.76ms p(99.9)=309.8ms 
     http_reqs......................: 32909   272.132272/s
     iteration_duration.............: avg=182.97ms min=40.08ms med=169.37ms max=407.32ms p(90)=235.38ms p(95)=241.13ms p(99.9)=313.03ms
     iterations.....................: 32809   271.305348/s
     success_rate...................: 100.00% ✓ 32809      ✗ 0    
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

