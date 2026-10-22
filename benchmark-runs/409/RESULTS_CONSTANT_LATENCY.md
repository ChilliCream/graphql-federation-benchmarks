## Overview for: `constant-vus-with-latency`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario executes a constant load of **50 VUs** over **120s** with a simulated **4ms IO delay** on each subgraph request.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| feddi-gateway | 3c75a7db8876 | 2,432 | 2,528 | 2,419 | 1.5% |  |
| fusion-nightly-net-11 | 16.7.0-p.30 | 2,264 | 2,328 | 2,251 | 1.1% |  |
| fusion-nightly-net-10 | 16.7.0-p.30 | 2,213 | 2,293 | 2,198 | 1.4% |  |
| fusion-net-10 | 16.6.9 | 1,892 | 1,947 | 1,881 | 1.2% |  |
| hive-router | v0.3.5 | 1,852 | 1,936 | 1,848 | 1.7% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.30 | 1,827 | 1,880 | 1,818 | 1.1% |  |
| cosmo | 0.359.0 | 1,324 | 1,367 | 1,312 | 1.5% |  |
| caliban | 3.2.0 | 1,300 | 1,357 | 1,293 | 1.6% |  |
| grafbase | 0.53.5 | 1,297 | 1,328 | 1,291 | 0.9% |  |
| hive-gateway-router-runtime | 2.15.2 | 497 | 515 | 493 | 1.4% |  |
| apollo-router | v2.18.0 | 437 | 455 | 435 | 1.6% |  |
| apollo-router-v3 | v3.0.0-preview.0 | 402 | 419 | 400 | 1.7% |  |
| apollo-gateway | 2.14.4 | 258 | 262 | 258 | 0.7% |  |
| hive-gateway | 2.15.2 | 256 | 262 | 254 | 1.3% |  |


### Details

<details>
  <summary>Summary for: feddi-gateway (HotChocolate subgraphs) (3c75a7db8876)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 885705      ✗ 0     
     data_received..................: 26 GB   213 MB/s
     data_sent......................: 355 MB  2.9 MB/s
     http_req_blocked...............: avg=2.7µs   min=811ns   med=1.97µs  max=3.81ms   p(90)=3.47µs  p(95)=4.4µs    p(99.9)=29.92µs
     http_req_connecting............: avg=326ns   min=0s      med=0s      max=3.77ms   p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=20.1ms  min=12.29ms med=19.43ms max=297.2ms  p(90)=24.02ms p(95)=25.99ms  p(99.9)=45.45ms
       { expected_response:true }...: avg=20.1ms  min=12.29ms med=19.43ms max=297.2ms  p(90)=24.02ms p(95)=25.99ms  p(99.9)=45.45ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 295335
     http_req_receiving.............: avg=79.17µs min=23.77µs med=47.04µs max=123.14ms p(90)=93.71µs p(95)=146.78µs p(99.9)=3.84ms 
     http_req_sending...............: avg=40.14µs min=4.45µs  med=8.45µs  max=188.08ms p(90)=16.98µs p(95)=82.68µs  p(99.9)=3.09ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=19.98ms min=12.22ms med=19.34ms max=296.51ms p(90)=23.89ms p(95)=25.81ms  p(99.9)=44.69ms
     http_reqs......................: 295335  2432.550694/s
     iteration_duration.............: avg=20.31ms min=12.43ms med=19.62ms max=307.99ms p(90)=24.21ms p(95)=26.2ms   p(99.9)=45.96ms
     iterations.....................: 295235  2431.727036/s
     success_rate...................: 100.00% ✓ 295235      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 824790      ✗ 0     
     data_received..................: 24 GB   199 MB/s
     data_sent......................: 331 MB  2.7 MB/s
     http_req_blocked...............: avg=3.36µs   min=932ns   med=2.44µs  max=13.07ms  p(90)=4.12µs  p(95)=4.97µs  p(99.9)=34.21µs
     http_req_connecting............: avg=344ns    min=0s      med=0s      max=3.5ms    p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=21.59ms  min=13ms    med=20.83ms max=290.08ms p(90)=26.2ms  p(95)=28.54ms p(99.9)=49.54ms
       { expected_response:true }...: avg=21.59ms  min=13ms    med=20.83ms max=290.08ms p(90)=26.2ms  p(95)=28.54ms p(99.9)=49.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 275030
     http_req_receiving.............: avg=409.62µs min=49.25µs med=86.06µs max=222.08ms p(90)=1.06ms  p(95)=2.02ms  p(99.9)=16.65ms
     http_req_sending...............: avg=43.19µs  min=4.65µs  med=8.98µs  max=199.72ms p(90)=19.24µs p(95)=90.45µs p(99.9)=3.7ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=21.14ms  min=12.82ms med=20.42ms max=289.48ms p(90)=25.6ms  p(95)=27.89ms p(99.9)=47.49ms
     http_reqs......................: 275030  2264.10669/s
     iteration_duration.............: avg=21.81ms  min=13.19ms med=21.04ms max=303.6ms  p(90)=26.4ms  p(95)=28.75ms p(99.9)=49.89ms
     iterations.....................: 274930  2263.283468/s
     success_rate...................: 100.00% ✓ 274930      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 806304      ✗ 0     
     data_received..................: 24 GB   194 MB/s
     data_sent......................: 323 MB  2.7 MB/s
     http_req_blocked...............: avg=3.23µs   min=892ns   med=2.48µs  max=4.18ms   p(90)=4.09µs  p(95)=4.88µs  p(99.9)=36.2µs 
     http_req_connecting............: avg=360ns    min=0s      med=0s      max=4.14ms   p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=22.1ms   min=13.12ms med=21.27ms max=296.83ms p(90)=27.31ms p(95)=29.77ms p(99.9)=50.55ms
       { expected_response:true }...: avg=22.1ms   min=13.12ms med=21.27ms max=296.83ms p(90)=27.31ms p(95)=29.77ms p(99.9)=50.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 268868
     http_req_receiving.............: avg=420.17µs min=50.26µs med=87.8µs  max=180.98ms p(90)=1.1ms   p(95)=1.93ms  p(99.9)=16.77ms
     http_req_sending...............: avg=42.44µs  min=4.53µs  med=9.1µs   max=165.5ms  p(90)=18.67µs p(95)=92.26µs p(99.9)=4.05ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=21.63ms  min=12.95ms med=20.84ms max=115.52ms p(90)=26.75ms p(95)=29.14ms p(99.9)=49.04ms
     http_reqs......................: 268868  2213.151702/s
     iteration_duration.............: avg=22.31ms  min=13.31ms med=21.48ms max=325.57ms p(90)=27.51ms p(95)=29.99ms p(99.9)=51.05ms
     iterations.....................: 268768  2212.328566/s
     success_rate...................: 100.00% ✓ 268768      ✗ 0     
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

     checks.........................: 100.00% ✓ 691845      ✗ 0     
     data_received..................: 20 GB   166 MB/s
     data_sent......................: 277 MB  2.3 MB/s
     http_req_blocked...............: avg=2.84µs   min=842ns   med=1.97µs  max=4.07ms   p(90)=3.67µs   p(95)=4.46µs  p(99.9)=30.3µs 
     http_req_connecting............: avg=443ns    min=0s      med=0s      max=4.02ms   p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=25.79ms  min=17.24ms med=25.2ms  max=292.09ms p(90)=30.19ms  p(95)=31.99ms p(99.9)=49.81ms
       { expected_response:true }...: avg=25.79ms  min=17.24ms med=25.2ms  max=292.09ms p(90)=30.19ms  p(95)=31.99ms p(99.9)=49.81ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 230715
     http_req_receiving.............: avg=289.46µs min=49.31µs med=89.78µs max=110.36ms p(90)=709.76µs p(95)=1.22ms  p(99.9)=8.63ms 
     http_req_sending...............: avg=32.53µs  min=4.44µs  med=8.3µs   max=124ms    p(90)=18.11µs  p(95)=31.37µs p(99.9)=1.7ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=25.47ms  min=17.16ms med=24.9ms  max=291.51ms p(90)=29.79ms  p(95)=31.56ms p(99.9)=48.73ms
     http_reqs......................: 230715  1892.116735/s
     iteration_duration.............: avg=26ms     min=17.42ms med=25.4ms  max=316.98ms p(90)=30.39ms  p(95)=32.2ms  p(99.9)=50.14ms
     iterations.....................: 230615  1891.296625/s
     success_rate...................: 100.00% ✓ 230615      ✗ 0     
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

     checks.........................: 100.00% ✓ 677601      ✗ 0     
     data_received..................: 20 GB   162 MB/s
     data_sent......................: 272 MB  2.2 MB/s
     http_req_blocked...............: avg=4.36µs  min=992ns   med=2.8µs   max=9.6ms    p(90)=4.53µs   p(95)=5.32µs   p(99.9)=37.86µs
     http_req_connecting............: avg=1.07µs  min=0s      med=0s      max=9.48ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=26.32ms min=18.15ms med=25.82ms max=278.48ms p(90)=30.14ms  p(95)=31.67ms  p(99.9)=50.53ms
       { expected_response:true }...: avg=26.32ms min=18.15ms med=25.82ms max=278.48ms p(90)=30.14ms  p(95)=31.67ms  p(99.9)=50.53ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 225967
     http_req_receiving.............: avg=82.14µs min=26.35µs med=55.88µs max=63.38ms  p(90)=102.66µs p(95)=133.57µs p(99.9)=2.5ms  
     http_req_sending...............: avg=37.57µs min=4.97µs  med=10.66µs max=206.05ms p(90)=19.21µs  p(95)=28.64µs  p(99.9)=1.89ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=26.2ms  min=18.01ms med=25.71ms max=276.82ms p(90)=30.02ms  p(95)=31.53ms  p(99.9)=49.41ms
     http_reqs......................: 225967  1852.868888/s
     iteration_duration.............: avg=26.55ms min=18.85ms med=26.03ms max=317.09ms p(90)=30.36ms  p(95)=31.9ms   p(99.9)=50.99ms
     iterations.....................: 225867  1852.048915/s
     success_rate...................: 100.00% ✓ 225867      ✗ 0     
     vus............................: 50      min=0         max=50  
     vus_max........................: 50      min=50        max=50
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.30)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 668352      ✗ 0     
     data_received..................: 20 GB   160 MB/s
     data_sent......................: 268 MB  2.2 MB/s
     http_req_blocked...............: avg=2.97µs   min=821ns   med=2µs     max=7.08ms   p(90)=3.83µs  p(95)=4.62µs  p(99.9)=33.63µs
     http_req_connecting............: avg=443ns    min=0s      med=0s      max=4ms      p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_duration..............: avg=26.7ms   min=17.79ms med=26.14ms max=296.32ms p(90)=31.26ms p(95)=33.1ms  p(99.9)=50.73ms
       { expected_response:true }...: avg=26.7ms   min=17.79ms med=26.14ms max=296.32ms p(90)=31.26ms p(95)=33.1ms  p(99.9)=50.73ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 222884
     http_req_receiving.............: avg=381.83µs min=50.38µs med=95.72µs max=114.71ms p(90)=1.07ms  p(95)=1.7ms   p(99.9)=9.07ms 
     http_req_sending...............: avg=32.99µs  min=4.34µs  med=8.29µs  max=117.13ms p(90)=18.65µs p(95)=38.3µs  p(99.9)=1.92ms 
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      p(99.9)=0s     
     http_req_waiting...............: avg=26.29ms  min=17.42ms med=25.74ms max=295.73ms p(90)=30.74ms p(95)=32.55ms p(99.9)=48.29ms
     http_reqs......................: 222884  1827.406054/s
     iteration_duration.............: avg=26.92ms  min=17.95ms med=26.34ms max=318.31ms p(90)=31.46ms p(95)=33.31ms p(99.9)=51.12ms
     iterations.....................: 222784  1826.586163/s
     success_rate...................: 100.00% ✓ 222784      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 484605     ✗ 0     
     data_received..................: 14 GB   116 MB/s
     data_sent......................: 194 MB  1.6 MB/s
     http_req_blocked...............: avg=3.04µs  min=962ns   med=2.11µs  max=3.97ms   p(90)=3.61µs   p(95)=4.37µs  p(99.9)=30.14µs 
     http_req_connecting............: avg=595ns   min=0s      med=0s      max=3.92ms   p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_duration..............: avg=36.91ms min=18.89ms med=36.33ms max=315.58ms p(90)=44.25ms  p(95)=46.79ms p(99.9)=60.36ms 
       { expected_response:true }...: avg=36.91ms min=18.89ms med=36.33ms max=315.58ms p(90)=44.25ms  p(95)=46.79ms p(99.9)=60.36ms 
     http_req_failed................: 0.00%   ✓ 0          ✗ 161635
     http_req_receiving.............: avg=75.15µs min=26.46µs med=60.07µs max=80.42ms  p(90)=102.89µs p(95)=124.9µs p(99.9)=861.56µs
     http_req_sending...............: avg=23.32µs min=4.64µs  med=9.81µs  max=76.17ms  p(90)=16.52µs  p(95)=21.03µs p(99.9)=998.53µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s      p(99.9)=0s      
     http_req_waiting...............: avg=36.81ms min=18.79ms med=36.24ms max=315.06ms p(90)=44.15ms  p(95)=46.67ms p(99.9)=60.09ms 
     http_reqs......................: 161635  1324.55167/s
     iteration_duration.............: avg=37.13ms min=21.38ms med=36.53ms max=325.64ms p(90)=44.45ms  p(95)=46.99ms p(99.9)=60.68ms 
     iterations.....................: 161535  1323.7322/s
     success_rate...................: 100.00% ✓ 161535     ✗ 0     
     vus............................: 50      min=0        max=50  
     vus_max........................: 50      min=50       max=50
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

     checks.........................: 100.00% ✓ 475920      ✗ 0     
     data_received..................: 14 GB   114 MB/s
     data_sent......................: 191 MB  1.6 MB/s
     http_req_blocked...............: avg=3.52µs  min=942ns   med=2.51µs  max=4.18ms   p(90)=4.37µs   p(95)=5.19µs   p(99.9)=40.48µs
     http_req_connecting............: avg=615ns   min=0s      med=0s      max=4.13ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.57ms min=19.66ms med=37ms    max=302.2ms  p(90)=44.74ms  p(95)=47.31ms  p(99.9)=60.69ms
       { expected_response:true }...: avg=37.57ms min=19.66ms med=37ms    max=302.2ms  p(90)=44.74ms  p(95)=47.31ms  p(99.9)=60.69ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 158740
     http_req_receiving.............: avg=75.69µs min=25.24µs med=60.6µs  max=20.38ms  p(90)=100.77µs p(95)=119.67µs p(99.9)=1.27ms 
     http_req_sending...............: avg=24.43µs min=5.06µs  med=11.49µs max=112.12ms p(90)=19.39µs  p(95)=23.42µs  p(99.9)=1.04ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.47ms min=19.58ms med=36.91ms max=301.64ms p(90)=44.63ms  p(95)=47.2ms   p(99.9)=60.46ms
     http_reqs......................: 158740  1300.594018/s
     iteration_duration.............: avg=37.81ms min=21.54ms med=37.22ms max=314.24ms p(90)=44.95ms  p(95)=47.53ms  p(99.9)=60.98ms
     iterations.....................: 158640  1299.774694/s
     success_rate...................: 100.00% ✓ 158640      ✗ 0     
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

     checks.........................: 100.00% ✓ 474603      ✗ 0     
     data_received..................: 14 GB   114 MB/s
     data_sent......................: 190 MB  1.6 MB/s
     http_req_blocked...............: avg=3.82µs  min=881ns   med=2.19µs  max=7.18ms   p(90)=4.69µs   p(95)=5.72µs   p(99.9)=44.09µs
     http_req_connecting............: avg=960ns   min=0s      med=0s      max=7.14ms   p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_duration..............: avg=37.66ms min=18.27ms med=37.43ms max=279.4ms  p(90)=44.33ms  p(95)=46.48ms  p(99.9)=62.55ms
       { expected_response:true }...: avg=37.66ms min=18.27ms med=37.43ms max=279.4ms  p(90)=44.33ms  p(95)=46.48ms  p(99.9)=62.55ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 158301
     http_req_receiving.............: avg=85.98µs min=27.1µs  med=53.93µs max=109.33ms p(90)=121.42µs p(95)=168.16µs p(99.9)=2.45ms 
     http_req_sending...............: avg=34.45µs min=4.77µs  med=9.12µs  max=227.28ms p(90)=22.82µs  p(95)=66.89µs  p(99.9)=2.25ms 
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s     
     http_req_waiting...............: avg=37.54ms min=18.13ms med=37.32ms max=279.1ms  p(90)=44.2ms   p(95)=46.34ms  p(99.9)=61.96ms
     http_reqs......................: 158301  1297.774182/s
     iteration_duration.............: avg=37.92ms min=21.15ms med=37.67ms max=323.21ms p(90)=44.55ms  p(95)=46.7ms   p(99.9)=62.8ms 
     iterations.....................: 158201  1296.954368/s
     success_rate...................: 100.00% ✓ 158201      ✗ 0     
     vus............................: 50      min=0         max=50  
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

     checks.........................: 100.00% ✓ 182238     ✗ 0    
     data_received..................: 5.3 GB  44 MB/s
     data_sent......................: 73 MB   597 kB/s
     http_req_blocked...............: avg=5.25µs  min=1.34µs  med=3.34µs  max=4.27ms   p(90)=4.94µs   p(95)=5.65µs   p(99.9)=49.2µs  
     http_req_connecting............: avg=1.63µs  min=0s      med=0s      max=4.23ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=98.39ms min=21.1ms  med=96.18ms max=329.93ms p(90)=118.85ms p(95)=128.38ms p(99.9)=226.75ms
       { expected_response:true }...: avg=98.39ms min=21.1ms  med=96.18ms max=329.93ms p(90)=118.85ms p(95)=128.38ms p(99.9)=226.75ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 60846
     http_req_receiving.............: avg=86.02µs min=32.62µs med=78.15µs max=79.23ms  p(90)=111.35µs p(95)=124.14µs p(99.9)=733.26µs
     http_req_sending...............: avg=25.62µs min=5.66µs  med=15.65µs max=139.94ms p(90)=21.98µs  p(95)=24.26µs  p(99.9)=585.89µs
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=98.28ms min=20.95ms med=96.08ms max=329.56ms p(90)=118.74ms p(95)=128.27ms p(99.9)=226.31ms
     http_reqs......................: 60846   497.474395/s
     iteration_duration.............: avg=98.78ms min=30.23ms med=96.45ms max=354.29ms p(90)=119.11ms p(95)=128.67ms p(99.9)=230.32ms
     iterations.....................: 60746   496.656799/s
     success_rate...................: 100.00% ✓ 60746      ✗ 0    
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

     checks.........................: 100.00% ✓ 160113     ✗ 0    
     data_received..................: 4.7 GB  38 MB/s
     data_sent......................: 64 MB   525 kB/s
     http_req_blocked...............: avg=5.95µs   min=1.35µs  med=3.79µs   max=3.83ms   p(90)=5.51µs   p(95)=6.18µs   p(99.9)=56.02µs 
     http_req_connecting............: avg=1.89µs   min=0s      med=0s       max=3.78ms   p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_duration..............: avg=111.99ms min=21.24ms med=110.08ms max=328.27ms p(90)=139.57ms p(95)=148.93ms p(99.9)=188.65ms
       { expected_response:true }...: avg=111.99ms min=21.24ms med=110.08ms max=328.27ms p(90)=139.57ms p(95)=148.93ms p(99.9)=188.65ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 53471
     http_req_receiving.............: avg=92.34µs  min=32.62µs med=84.91µs  max=106.96ms p(90)=117.53µs p(95)=130.59µs p(99.9)=596.4µs 
     http_req_sending...............: avg=24.62µs  min=5.77µs  med=17.53µs  max=115.73ms p(90)=23.23µs  p(95)=25.4µs   p(99.9)=588.12µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=111.87ms min=21.13ms med=109.97ms max=327.55ms p(90)=139.47ms p(95)=148.82ms p(99.9)=188.22ms
     http_reqs......................: 53471   437.128686/s
     iteration_duration.............: avg=112.45ms min=29.72ms med=110.4ms  max=361.35ms p(90)=139.86ms p(95)=149.26ms p(99.9)=190.05ms
     iterations.....................: 53371   436.31118/s
     success_rate...................: 100.00% ✓ 53371      ✗ 0    
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

     checks.........................: 100.00% ✓ 147660     ✗ 0    
     data_received..................: 4.3 GB  35 MB/s
     data_sent......................: 59 MB   484 kB/s
     http_req_blocked...............: avg=5.98µs   min=1.33µs  med=3.79µs   max=3.71ms   p(90)=5.47µs   p(95)=6.11µs   p(99.9)=196.54µs
     http_req_connecting............: avg=1.9µs    min=0s      med=0s       max=3.67ms   p(90)=0s       p(95)=0s       p(99.9)=72.69µs 
     http_req_duration..............: avg=121.45ms min=21.59ms med=119.75ms max=333.54ms p(90)=150.13ms p(95)=159.88ms p(99.9)=203.49ms
       { expected_response:true }...: avg=121.45ms min=21.59ms med=119.75ms max=333.54ms p(90)=150.13ms p(95)=159.88ms p(99.9)=203.49ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 49320
     http_req_receiving.............: avg=87.27µs  min=30.93µs med=83.52µs  max=2.61ms   p(90)=115.57µs p(95)=128.17µs p(99.9)=598.83µs
     http_req_sending...............: avg=23.18µs  min=6.12µs  med=17.03µs  max=64.42ms  p(90)=22.69µs  p(95)=24.83µs  p(99.9)=641.27µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=121.34ms min=21.44ms med=119.63ms max=332.83ms p(90)=150.03ms p(95)=159.75ms p(99.9)=203.4ms 
     http_reqs......................: 49320   402.991841/s
     iteration_duration.............: avg=121.93ms min=38.19ms med=120.05ms max=347.71ms p(90)=150.45ms p(95)=160.21ms p(99.9)=204.65ms
     iterations.....................: 49220   402.174745/s
     success_rate...................: 100.00% ✓ 49220      ✗ 0    
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

     checks.........................: 100.00% ✓ 94986     ✗ 0    
     data_received..................: 2.8 GB  23 MB/s
     data_sent......................: 38 MB   311 kB/s
     http_req_blocked...............: avg=6.75µs   min=1.43µs  med=3.69µs   max=9.04ms   p(90)=5.26µs   p(95)=5.88µs   p(99.9)=1.1ms   
     http_req_connecting............: avg=2.33µs   min=0s      med=0s       max=3.82ms   p(90)=0s       p(95)=0s       p(99.9)=995.02µs
     http_req_duration..............: avg=188.76ms min=22.76ms med=190.13ms max=351.73ms p(90)=202.6ms  p(95)=207.92ms p(99.9)=282.74ms
       { expected_response:true }...: avg=188.76ms min=22.76ms med=190.13ms max=351.73ms p(90)=202.6ms  p(95)=207.92ms p(99.9)=282.74ms
     http_req_failed................: 0.00%   ✓ 0         ✗ 31762
     http_req_receiving.............: avg=94.39µs  min=36.64µs med=88.55µs  max=28.66ms  p(90)=120.22µs p(95)=132.48µs p(99.9)=511.69µs
     http_req_sending...............: avg=28.18µs  min=6.44µs  med=17.74µs  max=92.57ms  p(90)=22.99µs  p(95)=24.86µs  p(99.9)=479.02µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=188.64ms min=22.59ms med=190ms    max=351.28ms p(90)=202.49ms p(95)=207.8ms  p(99.9)=282.65ms
     http_reqs......................: 31762   258.93659/s
     iteration_duration.............: avg=189.59ms min=50.41ms med=190.75ms max=365.13ms p(90)=202.9ms  p(95)=208.27ms p(99.9)=284.94ms
     iterations.....................: 31662   258.12135/s
     success_rate...................: 100.00% ✓ 31662     ✗ 0    
     vus............................: 50      min=0       max=50 
     vus_max........................: 50      min=50      max=50
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

     checks.........................: 100.00% ✓ 93570      ✗ 0    
     data_received..................: 2.7 GB  22 MB/s
     data_sent......................: 38 MB   307 kB/s
     http_req_blocked...............: avg=7.38µs   min=1.44µs  med=3.8µs    max=4.3ms    p(90)=5.41µs   p(95)=6.11µs   p(99.9)=1.53ms  
     http_req_connecting............: avg=3.3µs    min=0s      med=0s       max=4.25ms   p(90)=0s       p(95)=0s       p(99.9)=1.51ms  
     http_req_duration..............: avg=191.62ms min=17.66ms med=174.4ms  max=824.9ms  p(90)=237.29ms p(95)=262.22ms p(99.9)=734.76ms
       { expected_response:true }...: avg=191.62ms min=17.66ms med=174.4ms  max=824.9ms  p(90)=237.29ms p(95)=262.22ms p(99.9)=734.76ms
     http_req_failed................: 0.00%   ✓ 0          ✗ 31290
     http_req_receiving.............: avg=97.05µs  min=35.86µs med=91.83µs  max=5.46ms   p(90)=123.24µs p(95)=137.24µs p(99.9)=834.75µs
     http_req_sending...............: avg=33.06µs  min=7.11µs  med=18.72µs  max=121.76ms p(90)=23.89µs  p(95)=25.77µs  p(99.9)=545.75µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=191.49ms min=17.56ms med=174.28ms max=824.81ms p(90)=237.17ms p(95)=262.11ms p(99.9)=734.65ms
     http_reqs......................: 31290   256.029565/s
     iteration_duration.............: avg=192.47ms min=38.13ms med=174.83ms max=825.15ms p(90)=237.7ms  p(95)=262.85ms p(99.9)=735.02ms
     iterations.....................: 31190   255.211318/s
     success_rate...................: 100.00% ✓ 31190      ✗ 0    
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

