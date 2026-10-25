## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net-11 | 16.7.0-p.39 | 2,773 | 2,876 | 2,765 | 1.4% |  |
| fusion-nightly-aot-11 | 16.7.0-p.39 | 2,722 | 2,816 | 2,698 | 1.4% |  |
| fusion-nightly-net-10 | 16.7.0-p.39 | 2,699 | 2,800 | 2,690 | 1.5% |  |
| feddi-gateway | 3c75a7db8876 | 2,473 | 2,567 | 2,456 | 1.5% |  |
| fusion-nightly-fed-aot-11 | 16.7.0-p.39 | 2,447 | 2,544 | 2,413 | 1.7% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.39 | 2,420 | 2,521 | 2,397 | 1.7% |  |
| fusion-nightly-fed-net-11 | 16.7.0-p.39 | 2,412 | 2,516 | 2,388 | 1.8% |  |
| fusion-net-11 | 16.6.9 | 1,914 | 1,958 | 1,907 | 0.9% |  |
| fusion-net-10 | 16.6.9 | 1,896 | 1,926 | 1,881 | 0.8% |  |
| hive-router | v0.3.5 | 1,888 | 1,943 | 1,883 | 1.0% |  |
| fusion-aot-11 | 16.6.9 | 1,845 | 1,883 | 1,838 | 0.9% |  |
| fusion-fed-net-11 | 16.6.9 | 1,822 | 1,872 | 1,810 | 1.1% |  |
| fusion-fed-net-10 | 16.6.9 | 1,801 | 1,851 | 1,794 | 1.2% |  |
| fusion-fed-aot-11 | 16.6.9 | 1,760 | 1,803 | 1,743 | 1.2% |  |
| caliban | 3.2.0 | 1,400 | 1,454 | 1,395 | 1.5% |  |
| cosmo | 0.361.0 | 1,373 | 1,419 | 1,366 | 1.4% |  |
| grafbase | 0.53.5 | 1,301 | 1,326 | 1,293 | 1.0% |  |
| hive-gateway-router-runtime | 2.15.2 | 485 | 506 | 483 | 1.7% |  |
| apollo-router | v2.18.0 | 429 | 439 | 412 | 2.1% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 401 | 417 | 399 | 1.7% |  |
| apollo-gateway | 2.14.4 | 260 | 265 | 259 | 1.0% |  |
| hive-gateway | 2.15.2 | 250 | 256 | 248 | 1.1% |  |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 1006389     ✗ 0     
     data_received..................: 29 GB   243 MB/s
     data_sent......................: 403 MB  3.3 MB/s
     http_req_blocked...............: avg=3.2µs    min=961ns   med=2.28µs  max=16.43ms  p(90)=3.79µs  p(95)=4.6µs   p(99.9)=33.77µs
     http_req_connecting............: avg=373ns    min=0s      med=0s      max=6.34ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=17.66ms  min=8.41ms  med=16.77ms max=294.61ms p(90)=22.95ms p(95)=25.81ms p(99.9)=47.6ms 
       { expected_response:true }...: avg=17.66ms  min=8.41ms  med=16.77ms max=294.61ms p(90)=22.95ms p(95)=25.81ms p(99.9)=47.6ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 335563
     http_req_receiving.............: avg=732.07µs min=48.82µs med=86.85µs max=194.98ms p(90)=2.36ms  p(95)=3.9ms   p(99.9)=25.94ms
     http_req_sending...............: avg=47.8µs   min=4.47µs  med=8.37µs  max=117.9ms  p(90)=18.04µs p(95)=96.83µs p(99.9)=5.36ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=16.88ms  min=8.32ms  med=16.03ms max=281.88ms p(90)=21.78ms p(95)=24.58ms p(99.9)=44.49ms
     http_reqs......................: 335563  2773.31202/s
     iteration_duration.............: avg=17.87ms  min=8.59ms  med=16.97ms max=315.15ms p(90)=23.16ms p(95)=26.04ms p(99.9)=48.18ms
     iterations.....................: 335463  2772.485555/s
     success_rate...................: 100.00% ✓ 335463      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 988032      ✗ 0     
     data_received..................: 29 GB   239 MB/s
     data_sent......................: 396 MB  3.3 MB/s
     http_req_blocked...............: avg=2.55µs   min=811ns   med=1.8µs   max=11.81ms  p(90)=3.12µs  p(95)=3.96µs  p(99.9)=22.7µs 
     http_req_connecting............: avg=273ns    min=0s      med=0s      max=3.69ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=18ms     min=8.74ms  med=17.2ms  max=292.76ms p(90)=23.19ms p(95)=25.84ms p(99.9)=46ms   
       { expected_response:true }...: avg=18ms     min=8.74ms  med=17.2ms  max=292.76ms p(90)=23.19ms p(95)=25.84ms p(99.9)=46ms   
     http_req_failed................: 0.00%   ✓ 0           ✗ 329444
     http_req_receiving.............: avg=714.76µs min=49.94µs med=83.82µs max=260.35ms p(90)=2.29ms  p(95)=3.64ms  p(99.9)=23.07ms
     http_req_sending...............: avg=43.28µs  min=4.13µs  med=7.5µs   max=132.7ms  p(90)=15.9µs  p(95)=84.13µs p(99.9)=4.86ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.24ms  min=8.67ms  med=16.48ms max=292.03ms p(90)=22.06ms p(95)=24.59ms p(99.9)=43.86ms
     http_reqs......................: 329444  2722.523386/s
     iteration_duration.............: avg=18.2ms   min=8.91ms  med=17.39ms max=303.33ms p(90)=23.39ms p(95)=26.06ms p(99.9)=46.47ms
     iterations.....................: 329344  2721.696986/s
     success_rate...................: 100.00% ✓ 329344      ✗ 0     
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

     checks.........................: 100.00% ✓ 979803      ✗ 0     
     data_received..................: 29 GB   237 MB/s
     data_sent......................: 393 MB  3.2 MB/s
     http_req_blocked...............: avg=2.51µs   min=832ns   med=1.8µs   max=12.81ms  p(90)=3.05µs  p(95)=3.93µs  p(99.9)=23.38µs
     http_req_connecting............: avg=289ns    min=0s      med=0s      max=4.06ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=18.15ms  min=8.61ms  med=17.39ms max=288.06ms p(90)=23.48ms p(95)=26.07ms p(99.9)=47.36ms
       { expected_response:true }...: avg=18.15ms  min=8.61ms  med=17.39ms max=288.06ms p(90)=23.48ms p(95)=26.07ms p(99.9)=47.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 326701
     http_req_receiving.............: avg=849.48µs min=49.13µs med=87.44µs max=200.75ms p(90)=2.71ms  p(95)=4.07ms  p(99.9)=23.42ms
     http_req_sending...............: avg=45.02µs  min=4.36µs  med=7.56µs  max=116.72ms p(90)=16.42µs p(95)=86.56µs p(99.9)=5.26ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=17.26ms  min=8.45ms  med=16.47ms max=286.43ms p(90)=22.25ms p(95)=24.82ms p(99.9)=45.24ms
     http_reqs......................: 326701  2699.648106/s
     iteration_duration.............: avg=18.36ms  min=8.77ms  med=17.58ms max=298.43ms p(90)=23.68ms p(95)=26.29ms p(99.9)=47.84ms
     iterations.....................: 326601  2698.82177/s
     success_rate...................: 100.00% ✓ 326601      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 900624      ✗ 0     
     data_received..................: 26 GB   216 MB/s
     data_sent......................: 361 MB  3.0 MB/s
     http_req_blocked...............: avg=4.02µs  min=992ns   med=2.68µs  max=14.47ms  p(90)=4.59µs   p(95)=5.61µs  p(99.9)=40.07µs
     http_req_connecting............: avg=630ns   min=0s      med=0s      max=8.74ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.75ms min=12.3ms  med=19.02ms max=294.95ms p(90)=23.69ms  p(95)=25.96ms p(99.9)=46.71ms
       { expected_response:true }...: avg=19.75ms min=12.3ms  med=19.02ms max=294.95ms p(90)=23.69ms  p(95)=25.96ms p(99.9)=46.71ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 300308
     http_req_receiving.............: avg=86.97µs min=24.33µs med=49.02µs max=169.45ms p(90)=101.79µs p(95)=171.2µs p(99.9)=4.49ms 
     http_req_sending...............: avg=47.08µs min=4.72µs  med=10.11µs max=248.33ms p(90)=21.17µs  p(95)=99.51µs p(99.9)=3.54ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.62ms min=12.24ms med=18.91ms max=293.24ms p(90)=23.53ms  p(95)=25.74ms p(99.9)=46.01ms
     http_reqs......................: 300308  2473.703422/s
     iteration_duration.............: avg=19.97ms min=12.53ms med=19.22ms max=314.49ms p(90)=23.9ms   p(95)=26.19ms p(99.9)=47.22ms
     iterations.....................: 300208  2472.8797/s
     success_rate...................: 100.00% ✓ 300208      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 891621      ✗ 0     
     data_received..................: 26 GB   215 MB/s
     data_sent......................: 357 MB  2.9 MB/s
     http_req_blocked...............: avg=3.5µs    min=952ns   med=2.4µs   max=8.04ms   p(90)=4µs     p(95)=4.77µs  p(99.9)=34.43µs
     http_req_connecting............: avg=602ns    min=0s      med=0s      max=6.86ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=19.96ms  min=12.85ms med=19.13ms max=297.21ms p(90)=24.17ms p(95)=26.61ms p(99.9)=48.32ms
       { expected_response:true }...: avg=19.96ms  min=12.85ms med=19.13ms max=297.21ms p(90)=24.17ms p(95)=26.61ms p(99.9)=48.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 297307
     http_req_receiving.............: avg=387.62µs min=51.23µs med=86.6µs  max=38.23ms  p(90)=1ms     p(95)=1.93ms  p(99.9)=15.68ms
     http_req_sending...............: avg=41.92µs  min=4.56µs  med=8.6µs   max=142.29ms p(90)=17.64µs p(95)=91.84µs p(99.9)=3.65ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.53ms  min=12.2ms  med=18.73ms max=295.8ms  p(90)=23.59ms p(95)=25.98ms p(99.9)=46.71ms
     http_reqs......................: 297307  2447.590669/s
     iteration_duration.............: avg=20.17ms  min=13.05ms med=19.33ms max=311.96ms p(90)=24.38ms p(95)=26.83ms p(99.9)=48.63ms
     iterations.....................: 297207  2446.767415/s
     success_rate...................: 100.00% ✓ 297207      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 881706      ✗ 0     
     data_received..................: 26 GB   212 MB/s
     data_sent......................: 353 MB  2.9 MB/s
     http_req_blocked...............: avg=3.76µs   min=972ns   med=2.36µs  max=13.13ms  p(90)=3.98µs  p(95)=4.8µs   p(99.9)=34.6µs 
     http_req_connecting............: avg=878ns    min=0s      med=0s      max=8.92ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.19ms  min=12.33ms med=19.38ms max=272.01ms p(90)=24.82ms p(95)=27.03ms p(99.9)=48.64ms
       { expected_response:true }...: avg=20.19ms  min=12.33ms med=19.38ms max=272.01ms p(90)=24.82ms p(95)=27.03ms p(99.9)=48.64ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 294002
     http_req_receiving.............: avg=400.37µs min=49.7µs  med=85.74µs max=113.79ms p(90)=1.11ms  p(95)=2.13ms  p(99.9)=13.01ms
     http_req_sending...............: avg=42.54µs  min=4.75µs  med=8.63µs  max=181.02ms p(90)=18.12µs p(95)=92.23µs p(99.9)=3.73ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.74ms  min=12.25ms med=18.96ms max=270.95ms p(90)=24.22ms p(95)=26.41ms p(99.9)=47.4ms 
     http_reqs......................: 294002  2420.269912/s
     iteration_duration.............: avg=20.4ms   min=12.53ms med=19.59ms max=308.2ms  p(90)=25.03ms p(95)=27.24ms p(99.9)=49.01ms
     iterations.....................: 293902  2419.446697/s
     success_rate...................: 100.00% ✓ 293902      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-11 (HotChocolate subgraphs) (16.7.0-p.39)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 878808      ✗ 0     
     data_received..................: 26 GB   212 MB/s
     data_sent......................: 352 MB  2.9 MB/s
     http_req_blocked...............: avg=3.3µs    min=972ns   med=2.43µs  max=10.58ms  p(90)=4.07µs   p(95)=4.9µs   p(99.9)=38.18µs
     http_req_connecting............: avg=339ns    min=0s      med=0s      max=4.28ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=20.25ms  min=12.78ms med=19.42ms max=307.68ms p(90)=24.81ms  p(95)=27.23ms p(99.9)=48.36ms
       { expected_response:true }...: avg=20.25ms  min=12.78ms med=19.42ms max=307.68ms p(90)=24.81ms  p(95)=27.23ms p(99.9)=48.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 293036
     http_req_receiving.............: avg=388.97µs min=51.29µs med=86.93µs max=215.54ms p(90)=963.34µs p(95)=2.02ms  p(99.9)=14.84ms
     http_req_sending...............: avg=44.87µs  min=4.76µs  med=9.06µs  max=183.77ms p(90)=18.86µs  p(95)=94.97µs p(99.9)=3.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=19.82ms  min=12.69ms med=19.01ms max=301.88ms p(90)=24.23ms  p(95)=26.58ms p(99.9)=46.71ms
     http_reqs......................: 293036  2412.078805/s
     iteration_duration.............: avg=20.47ms  min=13ms    med=19.63ms max=318.81ms p(90)=25.02ms  p(95)=27.45ms p(99.9)=48.76ms
     iterations.....................: 292936  2411.255671/s
     success_rate...................: 100.00% ✓ 292936      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 699825      ✗ 0     
     data_received..................: 21 GB   168 MB/s
     data_sent......................: 280 MB  2.3 MB/s
     http_req_blocked...............: avg=2.87µs   min=842ns   med=1.96µs  max=4.48ms   p(90)=3.75µs  p(95)=4.49µs  p(99.9)=34.06µs
     http_req_connecting............: avg=444ns    min=0s      med=0s      max=4.44ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.49ms  min=17.1ms  med=24.91ms max=294.88ms p(90)=29.62ms p(95)=31.44ms p(99.9)=49.41ms
       { expected_response:true }...: avg=25.49ms  min=17.1ms  med=24.91ms max=294.88ms p(90)=29.62ms p(95)=31.44ms p(99.9)=49.41ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 233375
     http_req_receiving.............: avg=475.78µs min=50.29µs med=94.57µs max=169.68ms p(90)=1.42ms  p(95)=2.17ms  p(99.9)=12.95ms
     http_req_sending...............: avg=36.13µs  min=4.52µs  med=8.34µs  max=139.51ms p(90)=18.8µs  p(95)=50.26µs p(99.9)=2.18ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=24.98ms  min=17.02ms med=24.44ms max=294.46ms p(90)=28.88ms p(95)=30.59ms p(99.9)=47.03ms
     http_reqs......................: 233375  1914.129219/s
     iteration_duration.............: avg=25.71ms  min=17.29ms med=25.12ms max=303.22ms p(90)=29.82ms p(95)=31.65ms p(99.9)=49.79ms
     iterations.....................: 233275  1913.309025/s
     success_rate...................: 100.00% ✓ 233275      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 693252      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 278 MB  2.3 MB/s
     http_req_blocked...............: avg=3.4µs    min=962ns   med=2.49µs   max=9.39ms   p(90)=4.18µs  p(95)=4.92µs  p(99.9)=37.06µs
     http_req_connecting............: avg=421ns    min=0s      med=0s       max=5.28ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.73ms  min=16.53ms med=25.09ms  max=287.35ms p(90)=30.17ms p(95)=32.11ms p(99.9)=50.89ms
       { expected_response:true }...: avg=25.73ms  min=16.53ms med=25.09ms  max=287.35ms p(90)=30.17ms p(95)=32.11ms p(99.9)=50.89ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 231184
     http_req_receiving.............: avg=459.88µs min=49.05µs med=105.65µs max=177.68ms p(90)=1.27ms  p(95)=1.89ms  p(99.9)=10.09ms
     http_req_sending...............: avg=34.2µs   min=4.74µs  med=9.48µs   max=32.61ms  p(90)=18.91µs p(95)=48.7µs  p(99.9)=2.2ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.24ms  min=16.23ms med=24.62ms  max=285.24ms p(90)=29.53ms p(95)=31.39ms p(99.9)=49.74ms
     http_reqs......................: 231184  1896.385865/s
     iteration_duration.............: avg=25.95ms  min=16.74ms med=25.3ms   max=296.76ms p(90)=30.37ms p(95)=32.33ms p(99.9)=51.47ms
     iterations.....................: 231084  1895.565573/s
     success_rate...................: 100.00% ✓ 231084      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 690387      ✗ 0     
     data_received..................: 20 GB   165 MB/s
     data_sent......................: 277 MB  2.3 MB/s
     http_req_blocked...............: avg=3.03µs  min=841ns   med=2.12µs  max=4.92ms   p(90)=4.03µs  p(95)=4.88µs   p(99.9)=32.46µs
     http_req_connecting............: avg=420ns   min=0s      med=0s      max=3.9ms    p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=25.84ms min=17.98ms med=25.37ms max=304.14ms p(90)=29.5ms  p(95)=30.93ms  p(99.9)=48.49ms
       { expected_response:true }...: avg=25.84ms min=17.98ms med=25.37ms max=304.14ms p(90)=29.5ms  p(95)=30.93ms  p(99.9)=48.49ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 230229
     http_req_receiving.............: avg=76.25µs min=24.65µs med=48.26µs max=130.94ms p(90)=95.23µs p(95)=125.65µs p(99.9)=2.54ms 
     http_req_sending...............: avg=32.73µs min=4.37µs  med=8.97µs  max=190.4ms  p(90)=18.02µs p(95)=27.01µs  p(99.9)=1.6ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=25.73ms min=17.94ms med=25.28ms max=303.76ms p(90)=29.39ms p(95)=30.8ms   p(99.9)=47.25ms
     http_reqs......................: 230229  1888.124726/s
     iteration_duration.............: avg=26.06ms min=18.16ms med=25.58ms max=312.85ms p(90)=29.7ms  p(95)=31.13ms  p(99.9)=48.97ms
     iterations.....................: 230129  1887.304618/s
     success_rate...................: 100.00% ✓ 230129      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 674814      ✗ 0     
     data_received..................: 20 GB   162 MB/s
     data_sent......................: 270 MB  2.2 MB/s
     http_req_blocked...............: avg=3.05µs   min=832ns   med=2.03µs   max=9.14ms   p(90)=3.88µs  p(95)=4.64µs  p(99.9)=28.07µs
     http_req_connecting............: avg=473ns    min=0s      med=0s       max=5.02ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.44ms  min=17.11ms med=25.91ms  max=295.44ms p(90)=30.45ms p(95)=32.2ms  p(99.9)=51.18ms
       { expected_response:true }...: avg=26.44ms  min=17.11ms med=25.91ms  max=295.44ms p(90)=30.45ms p(95)=32.2ms  p(99.9)=51.18ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 225038
     http_req_receiving.............: avg=570.89µs min=48.83µs med=104.24µs max=267.95ms p(90)=1.66ms  p(95)=2.39ms  p(99.9)=13.91ms
     http_req_sending...............: avg=35.7µs   min=4.41µs  med=8.4µs    max=187.18ms p(90)=18.67µs p(95)=35.72µs p(99.9)=2.08ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.84ms  min=16.96ms med=25.35ms  max=288.23ms p(90)=29.59ms p(95)=31.23ms p(99.9)=49.13ms
     http_reqs......................: 225038  1845.587287/s
     iteration_duration.............: avg=26.66ms  min=17.39ms med=26.12ms  max=316.68ms p(90)=30.66ms p(95)=32.41ms p(99.9)=51.63ms
     iterations.....................: 224938  1844.767165/s
     success_rate...................: 100.00% ✓ 224938      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 666396      ✗ 0     
     data_received..................: 20 GB   160 MB/s
     data_sent......................: 267 MB  2.2 MB/s
     http_req_blocked...............: avg=3.35µs   min=781ns   med=1.9µs   max=7.79ms   p(90)=3.71µs  p(95)=4.49µs  p(99.9)=30.39µs
     http_req_connecting............: avg=880ns    min=0s      med=0s      max=7.05ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.78ms  min=17.91ms med=26.21ms max=266.81ms p(90)=31.21ms p(95)=33ms    p(99.9)=50.83ms
       { expected_response:true }...: avg=26.78ms  min=17.91ms med=26.21ms max=266.81ms p(90)=31.21ms p(95)=33ms    p(99.9)=50.83ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 222232
     http_req_receiving.............: avg=464.35µs min=48.05µs med=93.99µs max=35.69ms  p(90)=1.37ms  p(95)=2.13ms  p(99.9)=11.82ms
     http_req_sending...............: avg=33.52µs  min=4.43µs  med=8.09µs  max=168.62ms p(90)=18.56µs p(95)=33.61µs p(99.9)=2.07ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.28ms  min=17.79ms med=25.75ms max=264.99ms p(90)=30.48ms p(95)=32.17ms p(99.9)=49.09ms
     http_reqs......................: 222232  1822.280077/s
     iteration_duration.............: avg=27ms     min=18.22ms med=26.42ms max=299.7ms  p(90)=31.41ms p(95)=33.2ms  p(99.9)=51.14ms
     iterations.....................: 222132  1821.460087/s
     success_rate...................: 100.00% ✓ 222132      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 658851      ✗ 0     
     data_received..................: 19 GB   158 MB/s
     data_sent......................: 264 MB  2.2 MB/s
     http_req_blocked...............: avg=2.94µs   min=842ns   med=2.01µs   max=8.4ms    p(90)=3.69µs  p(95)=4.44µs  p(99.9)=28.14µs
     http_req_connecting............: avg=407ns    min=0s      med=0s       max=3.68ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=27.09ms  min=18.15ms med=26.5ms   max=322.42ms p(90)=31.78ms p(95)=33.65ms p(99.9)=51.75ms
       { expected_response:true }...: avg=27.09ms  min=18.15ms med=26.5ms   max=322.42ms p(90)=31.78ms p(95)=33.65ms p(99.9)=51.75ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 219717
     http_req_receiving.............: avg=468.46µs min=48.58µs med=101.77µs max=281.14ms p(90)=1.23ms  p(95)=1.86ms  p(99.9)=12.15ms
     http_req_sending...............: avg=33.23µs  min=4.61µs  med=8.52µs   max=27.89ms  p(90)=18.77µs p(95)=49.99µs p(99.9)=2.14ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.59ms  min=18.02ms med=26.05ms  max=69.46ms  p(90)=31.15ms p(95)=32.95ms p(99.9)=48.87ms
     http_reqs......................: 219717  1801.362386/s
     iteration_duration.............: avg=27.31ms  min=18.34ms med=26.71ms  max=347.21ms p(90)=31.99ms p(95)=33.86ms p(99.9)=52.08ms
     iterations.....................: 219617  1800.542531/s
     success_rate...................: 100.00% ✓ 219617      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 643893      ✗ 0     
     data_received..................: 19 GB   154 MB/s
     data_sent......................: 258 MB  2.1 MB/s
     http_req_blocked...............: avg=3.63µs   min=990ns   med=2.61µs   max=10.37ms  p(90)=4.36µs  p(95)=5.1µs   p(99.9)=36.15µs
     http_req_connecting............: avg=531ns    min=0s      med=0s       max=5.94ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=27.72ms  min=17.5ms  med=27.2ms   max=289.92ms p(90)=31.89ms p(95)=33.71ms p(99.9)=52.21ms
       { expected_response:true }...: avg=27.72ms  min=17.5ms  med=27.2ms   max=289.92ms p(90)=31.89ms p(95)=33.71ms p(99.9)=52.21ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 214731
     http_req_receiving.............: avg=635.69µs min=50.82µs med=121.95µs max=234.83ms p(90)=1.72ms  p(95)=2.42ms  p(99.9)=15.05ms
     http_req_sending...............: avg=34.43µs  min=4.8µs   med=9.89µs   max=69.15ms  p(90)=19.55µs p(95)=51.89µs p(99.9)=1.91ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=27.05ms  min=17.41ms med=26.57ms  max=289.53ms p(90)=30.97ms p(95)=32.69ms p(99.9)=49.54ms
     http_reqs......................: 214731  1760.617351/s
     iteration_duration.............: avg=27.94ms  min=17.7ms  med=27.42ms  max=299.79ms p(90)=32.1ms  p(95)=33.92ms p(99.9)=52.62ms
     iterations.....................: 214631  1759.797433/s
     success_rate...................: 100.00% ✓ 214631      ✗ 0     
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

     checks.........................: 100.00% ✓ 512211      ✗ 0     
     data_received..................: 15 GB   122 MB/s
     data_sent......................: 205 MB  1.7 MB/s
     http_req_blocked...............: avg=3.83µs  min=932ns   med=2.68µs  max=4.61ms   p(90)=4.9µs    p(95)=5.77µs   p(99.9)=33.74µs
     http_req_connecting............: avg=678ns   min=0s      med=0s      max=4.57ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=34.89ms min=19.31ms med=34.38ms max=299.27ms p(90)=40.8ms   p(95)=43.06ms  p(99.9)=58.09ms
       { expected_response:true }...: avg=34.89ms min=19.31ms med=34.38ms max=299.27ms p(90)=40.8ms   p(95)=43.06ms  p(99.9)=58.09ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 170837
     http_req_receiving.............: avg=81.91µs min=24.16µs med=61.65µs max=149.61ms p(90)=108.55µs p(95)=131.99µs p(99.9)=1.64ms 
     http_req_sending...............: avg=30.77µs min=4.74µs  med=11.77µs max=233.11ms p(90)=21.23µs  p(95)=26.21µs  p(99.9)=1.26ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=34.77ms min=19.18ms med=34.28ms max=299.02ms p(90)=40.68ms  p(95)=42.94ms  p(99.9)=56.95ms
     http_reqs......................: 170837  1400.050092/s
     iteration_duration.............: avg=35.13ms min=21.46ms med=34.6ms  max=310.34ms p(90)=41.02ms  p(95)=43.28ms  p(99.9)=58.86ms
     iterations.....................: 170737  1399.230568/s
     success_rate...................: 100.00% ✓ 170737      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 502659      ✗ 0     
     data_received..................: 15 GB   120 MB/s
     data_sent......................: 201 MB  1.7 MB/s
     http_req_blocked...............: avg=3.87µs  min=1.07µs  med=2.96µs  max=3.7ms    p(90)=4.78µs   p(95)=5.6µs    p(99.9)=38.27µs
     http_req_connecting............: avg=547ns   min=0s      med=0s      max=3.65ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=35.56ms min=18.79ms med=34.97ms max=295.26ms p(90)=42.49ms  p(95)=44.94ms  p(99.9)=58.98ms
       { expected_response:true }...: avg=35.56ms min=18.79ms med=34.97ms max=295.26ms p(90)=42.49ms  p(95)=44.94ms  p(99.9)=58.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 167653
     http_req_receiving.............: avg=83.89µs min=27.16µs med=65.72µs max=111.58ms p(90)=111.18µs p(95)=134.24µs p(99.9)=1.34ms 
     http_req_sending...............: avg=31.57µs min=5.18µs  med=12.26µs max=111.05ms p(90)=20.35µs  p(95)=25.78µs  p(99.9)=1.22ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=35.45ms min=18.64ms med=34.86ms max=294.75ms p(90)=42.37ms  p(95)=44.81ms  p(99.9)=58.45ms
     http_reqs......................: 167653  1373.901609/s
     iteration_duration.............: avg=35.8ms  min=20.06ms med=35.19ms max=309.25ms p(90)=42.71ms  p(95)=45.16ms  p(99.9)=59.47ms
     iterations.....................: 167553  1373.082117/s
     success_rate...................: 100.00% ✓ 167553      ✗ 0     
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

     checks.........................: 100.00% ✓ 475938      ✗ 0     
     data_received..................: 14 GB   114 MB/s
     data_sent......................: 191 MB  1.6 MB/s
     http_req_blocked...............: avg=3.38µs  min=841ns   med=2.17µs  max=4.06ms   p(90)=4.7µs    p(95)=5.81µs  p(99.9)=40.93µs
     http_req_connecting............: avg=611ns   min=0s      med=0s      max=4.02ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=37.56ms min=17.93ms med=37.24ms max=315.88ms p(90)=44.18ms  p(95)=46.25ms p(99.9)=63.55ms
       { expected_response:true }...: avg=37.56ms min=17.93ms med=37.24ms max=315.88ms p(90)=44.18ms  p(95)=46.25ms p(99.9)=63.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 158746
     http_req_receiving.............: avg=87.12µs min=26.49µs med=54.56µs max=166.67ms p(90)=123.02µs p(95)=167.6µs p(99.9)=2.07ms 
     http_req_sending...............: avg=34.53µs min=4.78µs  med=9.27µs  max=198.42ms p(90)=23.37µs  p(95)=38.18µs p(99.9)=1.81ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=37.44ms min=17.75ms med=37.13ms max=302.73ms p(90)=44.05ms  p(95)=46.11ms p(99.9)=62.05ms
     http_reqs......................: 158746  1301.317209/s
     iteration_duration.............: avg=37.81ms min=21.33ms med=37.48ms max=326.18ms p(90)=44.39ms  p(95)=46.46ms p(99.9)=63.87ms
     iterations.....................: 158646  1300.497461/s
     success_rate...................: 100.00% ✓ 158646      ✗ 0     
     vus............................: 8       min=0         max=50  
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

     checks.........................: 100.00% ✓ 178014     ✗ 0    
     data_received..................: 5.2 GB  43 MB/s
     data_sent......................: 71 MB   584 kB/s
     http_req_blocked...............: avg=3.7µs    min=1.1µs   med=2.78µs  max=1.83ms   p(90)=4.28µs   p(95)=4.91µs   p(99.9)=55.7µs  
     http_req_connecting............: avg=687ns    min=0s      med=0s      max=1.79ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=100.74ms min=21.1ms  med=98.06ms max=306.97ms p(90)=124.51ms p(95)=134.81ms p(99.9)=231.09ms
       { expected_response:true }...: avg=100.74ms min=21.1ms  med=98.06ms max=306.97ms p(90)=124.51ms p(95)=134.81ms p(99.9)=231.09ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 59438
     http_req_receiving.............: avg=83.99µs  min=29.9µs  med=75.17µs max=84.93ms  p(90)=109.39µs p(95)=122.02µs p(99.9)=661.14µs
     http_req_sending...............: avg=19µs     min=5.08µs  med=13.55µs max=72.87ms  p(90)=19.58µs  p(95)=21.59µs  p(99.9)=540.66µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=100.64ms min=21ms    med=97.96ms max=300.38ms p(90)=124.42ms p(95)=134.71ms p(99.9)=230.76ms
     http_reqs......................: 59438   485.928481/s
     iteration_duration.............: avg=101.13ms min=39.34ms med=98.33ms max=316.85ms p(90)=124.76ms p(95)=135.1ms  p(99.9)=233.17ms
     iterations.....................: 59338   485.110943/s
     success_rate...................: 100.00% ✓ 59338      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 157368     ✗ 0    
     data_received..................: 4.6 GB  38 MB/s
     data_sent......................: 63 MB   516 kB/s
     http_req_blocked...............: avg=4.35µs   min=1.04µs  med=3.27µs   max=2.78ms   p(90)=4.83µs   p(95)=5.44µs   p(99.9)=68.61µs 
     http_req_connecting............: avg=862ns    min=0s      med=0s       max=2.74ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=113.95ms min=21.49ms med=112.12ms max=346.36ms p(90)=142.31ms p(95)=151.65ms p(99.9)=193.51ms
       { expected_response:true }...: avg=113.95ms min=21.49ms med=112.12ms max=346.36ms p(90)=142.31ms p(95)=151.65ms p(99.9)=193.51ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 52556
     http_req_receiving.............: avg=176.96µs min=29.31µs med=84.53µs  max=237.18ms p(90)=115.46µs p(95)=128.12µs p(99.9)=863.7µs 
     http_req_sending...............: avg=19.95µs  min=5.05µs  med=16.44µs  max=17.69ms  p(90)=21.63µs  p(95)=23.59µs  p(99.9)=517.65µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=113.76ms min=21.22ms med=111.99ms max=218.14ms p(90)=142.11ms p(95)=151.41ms p(99.9)=188.08ms
     http_reqs......................: 52556   429.639867/s
     iteration_duration.............: avg=114.39ms min=30.66ms med=112.42ms max=360.02ms p(90)=142.6ms  p(95)=151.98ms p(99.9)=194.89ms
     iterations.....................: 52456   428.822378/s
     success_rate...................: 100.00% ✓ 52456      ✗ 0    
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

     checks.........................: 100.00% ✓ 147063     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   482 kB/s
     http_req_blocked...............: avg=5.47µs   min=1.34µs  med=3.9µs    max=3.76ms   p(90)=5.62µs   p(95)=6.28µs   p(99.9)=139.05µs
     http_req_connecting............: avg=1.2µs    min=0s      med=0s       max=2.76ms   p(90)=0s       p(95)=0s       p(99.9)=60.65µs 
     http_req_duration..............: avg=121.93ms min=21.54ms med=120.19ms max=346.91ms p(90)=150.52ms p(95)=160.67ms p(99.9)=207.57ms
       { expected_response:true }...: avg=121.93ms min=21.54ms med=120.19ms max=346.91ms p(90)=150.52ms p(95)=160.67ms p(99.9)=207.57ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49121
     http_req_receiving.............: avg=91.33µs  min=29.27µs med=85.24µs  max=111.66ms p(90)=117.97µs p(95)=131.06µs p(99.9)=577.07µs
     http_req_sending...............: avg=35.63µs  min=5.83µs  med=17.68µs  max=138.07ms p(90)=23.28µs  p(95)=25.39µs  p(99.9)=734.07µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.8ms  min=21.43ms med=120.07ms max=346.53ms p(90)=150.4ms  p(95)=160.54ms p(99.9)=207.13ms
     http_reqs......................: 49121   401.399087/s
     iteration_duration.............: avg=122.42ms min=33.45ms med=120.51ms max=355.13ms p(90)=150.83ms p(95)=160.98ms p(99.9)=208.34ms
     iterations.....................: 49021   400.581923/s
     success_rate...................: 100.00% ✓ 49021      ✗ 0    
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

     checks.........................: 100.00% ✓ 95412      ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   312 kB/s
     http_req_blocked...............: avg=7.15µs   min=1.55µs  med=3.85µs   max=3.51ms   p(90)=5.48µs   p(95)=6.12µs   p(99.9)=1.73ms  
     http_req_connecting............: avg=2.94µs   min=0s      med=0s       max=3.47ms   p(90)=0s       p(95)=0s       p(99.9)=1.66ms  
     http_req_duration..............: avg=187.89ms min=23.56ms med=187.06ms max=405.36ms p(90)=204.75ms p(95)=209.97ms p(99.9)=272.99ms
       { expected_response:true }...: avg=187.89ms min=23.56ms med=187.06ms max=405.36ms p(90)=204.75ms p(95)=209.97ms p(99.9)=272.99ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31904
     http_req_receiving.............: avg=94.84µs  min=36.35µs med=90.28µs  max=5.65ms   p(90)=122.2µs  p(95)=135.39µs p(99.9)=576.51µs
     http_req_sending...............: avg=40.75µs  min=6.69µs  med=19.11µs  max=127.11ms p(90)=24.47µs  p(95)=26.58µs  p(99.9)=503.25µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=187.76ms min=23.4ms  med=186.93ms max=404.85ms p(90)=204.63ms p(95)=209.81ms p(99.9)=272.83ms
     http_reqs......................: 31904   260.095931/s
     iteration_duration.............: avg=188.75ms min=55.78ms med=187.51ms max=420.01ms p(90)=205.05ms p(95)=210.32ms p(99.9)=278.48ms
     iterations.....................: 31804   259.280685/s
     success_rate...................: 100.00% ✓ 31804      ✗ 0    
     vus............................: 50      min=0        max=50 
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

     checks.........................: 100.00% ✓ 91377      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 37 MB   300 kB/s
     http_req_blocked...............: avg=7.34µs   min=1.56µs  med=3.7µs    max=4.24ms   p(90)=5.2µs    p(95)=5.85µs   p(99.9)=1.63ms  
     http_req_connecting............: avg=3.29µs   min=0s      med=0s       max=4.2ms    p(90)=0s       p(95)=0s       p(99.9)=1.5ms   
     http_req_duration..............: avg=196.25ms min=17.58ms med=181.27ms max=784.99ms p(90)=232.95ms p(95)=258.01ms p(99.9)=712.4ms 
       { expected_response:true }...: avg=196.25ms min=17.58ms med=181.27ms max=784.99ms p(90)=232.95ms p(95)=258.01ms p(99.9)=712.4ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 30559
     http_req_receiving.............: avg=100.11µs min=38.35µs med=89.52µs  max=64.06ms  p(90)=121.33µs p(95)=134.17µs p(99.9)=1.13ms  
     http_req_sending...............: avg=24.98µs  min=6.82µs  med=17.52µs  max=58.95ms  p(90)=22.47µs  p(95)=24.4µs   p(99.9)=526.29µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=196.12ms min=17.45ms med=181.15ms max=784.89ms p(90)=232.83ms p(95)=257.87ms p(99.9)=712.28ms
     http_reqs......................: 30559   250.099445/s
     iteration_duration.............: avg=197.12ms min=48.63ms med=181.69ms max=785.26ms p(90)=233.39ms p(95)=258.75ms p(99.9)=712.7ms 
     iterations.....................: 30459   249.28103/s
     success_rate...................: 100.00% ✓ 30459      ✗ 0    
     vus............................: 49      min=0        max=50 
     vus_max........................: 50      min=50       max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

