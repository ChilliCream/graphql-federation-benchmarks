## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 subgraphs and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 6 runs of 60s each. The first run is a full-duration warmup (discarded). The remaining 5 runs are measured. Results are ranked by **median RPS** across the 5 measured runs, with best/worst/CV% reported for transparency. Peak Memory is the gateway's peak RSS during the median run; Memory per Request divides it by the median RPS (lower means less memory for the same throughput).

This scenario is a burst stress test with peaks up to **500 VUs** over **60s**.


### Results

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Peak Memory | Memory per Request | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | ----------: | -----------------: | :---- |
| fusion-net-11 | 16.7.3 | 4,724 | 4,760 | 4,720 | 0.3% | 434 MB | 94.1 KB |  |
| fusion-nightly-net-11 | 16.8.0-p.9 | 4,624 | 4,731 | 4,458 | 2.2% | 425 MB | 94.1 KB |  |
| fusion-aot-11 | 16.7.3 | 4,598 | 4,611 | 4,553 | 0.5% | 155 MB | 34.5 KB |  |
| fusion-nightly-fed-net-11 | 16.8.0-p.9 | 4,591 | 4,608 | 4,466 | 1.3% | 435 MB | 97.1 KB |  |
| fusion-fed-net-11 | 16.7.3 | 4,406 | 4,443 | 4,385 | 0.5% | 433 MB | 100.7 KB |  |
| fusion-nightly-aot-11 | 16.8.0-p.9 | 4,391 | 4,486 | 4,374 | 1.0% | 176 MB | 41.0 KB |  |
| fusion-fed-aot-11 | 16.7.3 | 4,264 | 4,285 | 4,217 | 0.8% | 198 MB | 47.6 KB |  |
| fusion-nightly-fed-aot-11 | 16.8.0-p.9 | 4,213 | 4,267 | 4,196 | 0.7% | 158 MB | 38.3 KB |  |
| feddi-gateway | 2026-10-25-0247 | 4,187 | 4,212 | 4,103 | 1.0% | 2,301 MB | 562.6 KB |  |
| hive-router | v0.3.10 | 2,730 | 2,745 | 2,694 | 0.7% | 166 MB | 62.2 KB |  |
| cosmo | 0.365.2 | 1,340 | 1,341 | 1,337 | 0.1% | 586 MB | 448.1 KB |  |
| caliban | 3.2.0 | 1,325 | 1,327 | 1,324 | 0.1% | 10,873 MB | 8,403.3 KB |  |
| hive-gateway-router-runtime | 2.15.6 | 492 | 493 | 488 | 0.4% | 3,165 MB | 6,586.9 KB |  |
| hive-gateway | 2.15.6 | 248 | 250 | 246 | 0.6% | 3,822 MB | 15,780.2 KB |  |
| apollo-gateway | 2.14.4 | 242 | 242 | 241 | 0.2% | 2,461 MB | 10,412.2 KB |  |
| apollo-router | v2.19.0 | — | — | — | — | — | — | non-compatible response (5357 across 5/5 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | — | — | non-compatible response (5722 across 5/5 runs) |
| grafbase | 0.53.5 | — | — | — | — | — | — | non-compatible response (149706 across 5/5 runs) |


### Details

<details>
  <summary>Summary for: fusion-net-11 (HotChocolate subgraphs) (16.7.3)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 861006      ✗ 0     
     data_received..................: 25 GB   413 MB/s
     data_sent......................: 346 MB  5.7 MB/s
     http_req_blocked...............: avg=65.06µs  min=791ns    med=2.1µs   max=147.49ms p(90)=3.78µs   p(95)=4.98µs   p(99.9)=23.63ms 
     http_req_connecting............: avg=61.68µs  min=0s       med=0s      max=147.4ms  p(90)=0s       p(95)=0s       p(99.9)=22.98ms 
     http_req_duration..............: avg=47.53ms  min=779.83µs med=40.22ms max=273.29ms p(90)=99.66ms  p(95)=123.14ms p(99.9)=174.26ms
       { expected_response:true }...: avg=47.53ms  min=779.83µs med=40.22ms max=273.29ms p(90)=99.66ms  p(95)=123.14ms p(99.9)=174.26ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 288002
     http_req_receiving.............: avg=324.66µs min=22.16µs  med=51.75µs max=152.54ms p(90)=203.57µs p(95)=357.09µs p(99.9)=44.4ms  
     http_req_sending...............: avg=148.16µs min=4.1µs    med=8.6µs   max=162.79ms p(90)=17.78µs  p(95)=116.6µs  p(99.9)=26.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=47.06ms  min=731.28µs med=39.89ms max=270.66ms p(90)=98.49ms  p(95)=121.97ms p(99.9)=170.35ms
     http_reqs......................: 288002  4724.971073/s
     iteration_duration.............: avg=49.63ms  min=1.21ms   med=41.19ms max=348.62ms p(90)=104.42ms p(95)=130.13ms p(99.9)=207.18ms
     iterations.....................: 287002  4708.565038/s
     success_rate...................: 100.00% ✓ 287002      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 842928      ✗ 0     
     data_received..................: 25 GB   405 MB/s
     data_sent......................: 339 MB  5.6 MB/s
     http_req_blocked...............: avg=71.17µs  min=981ns    med=2.59µs  max=167.63ms p(90)=4.16µs   p(95)=5.35µs   p(99.9)=27.84ms 
     http_req_connecting............: avg=67.36µs  min=0s       med=0s      max=159.71ms p(90)=0s       p(95)=0s       p(99.9)=27.71ms 
     http_req_duration..............: avg=48.74ms  min=755.79µs med=41.42ms max=250.08ms p(90)=102.75ms p(95)=127.01ms p(99.9)=180.68ms
       { expected_response:true }...: avg=48.74ms  min=755.79µs med=41.42ms max=250.08ms p(90)=102.75ms p(95)=127.01ms p(99.9)=180.68ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 281976
     http_req_receiving.............: avg=355.16µs min=26.52µs  med=53.13µs max=133.69ms p(90)=215.73µs p(95)=370.74µs p(99.9)=48.16ms 
     http_req_sending...............: avg=153.16µs min=3.95µs   med=9.23µs  max=171.13ms p(90)=17.77µs  p(95)=120.16µs p(99.9)=27.82ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.23ms  min=716.96µs med=41.1ms  max=249.92ms p(90)=101.52ms p(95)=125.52ms p(99.9)=174.45ms
     http_reqs......................: 281976  4624.735583/s
     iteration_duration.............: avg=50.69ms  min=1.21ms   med=42.26ms max=374.79ms p(90)=107.1ms  p(95)=132.62ms p(99.9)=208.15ms
     iterations.....................: 280976  4608.334415/s
     success_rate...................: 100.00% ✓ 280976      ✗ 0     
     vus............................: 55      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 839061      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=55.78µs  min=821ns    med=2.06µs  max=143.38ms p(90)=3.72µs   p(95)=4.9µs    p(99.9)=18.57ms 
     http_req_connecting............: avg=52.42µs  min=0s       med=0s      max=139.75ms p(90)=0s       p(95)=0s       p(99.9)=18.33ms 
     http_req_duration..............: avg=49.7ms   min=827.57µs med=41.81ms max=294.3ms  p(90)=106.1ms  p(95)=130.8ms  p(99.9)=186.88ms
       { expected_response:true }...: avg=49.7ms   min=827.57µs med=41.81ms max=294.3ms  p(90)=106.1ms  p(95)=130.8ms  p(99.9)=186.88ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280687
     http_req_receiving.............: avg=301.85µs min=22.52µs  med=49.53µs max=114.43ms p(90)=210.94µs p(95)=376.18µs p(99.9)=42.04ms 
     http_req_sending...............: avg=137.99µs min=4.2µs    med=8.54µs  max=138.97ms p(90)=17.75µs  p(95)=122.86µs p(99.9)=24.49ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=49.26ms  min=790.26µs med=41.52ms max=253.72ms p(90)=105.22ms p(95)=129.7ms  p(99.9)=177.7ms 
     http_reqs......................: 280687  4598.295208/s
     iteration_duration.............: avg=50.93ms  min=1.44ms   med=42.47ms max=318.41ms p(90)=108.42ms p(95)=134.01ms p(99.9)=204.7ms 
     iterations.....................: 279687  4581.91292/s
     success_rate...................: 100.00% ✓ 279687      ✗ 0     
     vus............................: 59      min=0         max=498 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 838713      ✗ 0     
     data_received..................: 25 GB   402 MB/s
     data_sent......................: 337 MB  5.5 MB/s
     http_req_blocked...............: avg=58.25µs  min=781ns    med=2.07µs  max=128.29ms p(90)=3.8µs    p(95)=5.03µs   p(99.9)=19.18ms 
     http_req_connecting............: avg=54.95µs  min=0s       med=0s      max=128.02ms p(90)=0s       p(95)=0s       p(99.9)=19.1ms  
     http_req_duration..............: avg=49.42ms  min=898.03µs med=41.6ms  max=306.02ms p(90)=105.21ms p(95)=130.08ms p(99.9)=188.58ms
       { expected_response:true }...: avg=49.42ms  min=898.03µs med=41.6ms  max=306.02ms p(90)=105.21ms p(95)=130.08ms p(99.9)=188.58ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 280571
     http_req_receiving.............: avg=392.25µs min=25.79µs  med=52.26µs max=106.43ms p(90)=216.53µs p(95)=381.67µs p(99.9)=60.18ms 
     http_req_sending...............: avg=141.02µs min=3.98µs   med=8.47µs  max=254.09ms p(90)=17.97µs  p(95)=119.91µs p(99.9)=26.01ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=48.89ms  min=851.15µs med=41.29ms max=305.65ms p(90)=104.01ms p(95)=128.83ms p(99.9)=176.99ms
     http_reqs......................: 280571  4591.903112/s
     iteration_duration.............: avg=50.94ms  min=1.41ms   med=42.29ms max=343.5ms  p(90)=108.7ms  p(95)=134.64ms p(99.9)=209.95ms
     iterations.....................: 279571  4575.536833/s
     success_rate...................: 100.00% ✓ 279571      ✗ 0     
     vus............................: 60      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 804939      ✗ 0     
     data_received..................: 24 GB   386 MB/s
     data_sent......................: 324 MB  5.3 MB/s
     http_req_blocked...............: avg=67.74µs  min=872ns    med=2.72µs  max=133.8ms  p(90)=4.39µs   p(95)=5.59µs   p(99.9)=23.51ms 
     http_req_connecting............: avg=63.1µs   min=0s       med=0s      max=133.59ms p(90)=0s       p(95)=0s       p(99.9)=23.12ms 
     http_req_duration..............: avg=51.35ms  min=908.28µs med=43.16ms max=315.44ms p(90)=109.51ms p(95)=136.46ms p(99.9)=190.52ms
       { expected_response:true }...: avg=51.35ms  min=908.28µs med=43.16ms max=315.44ms p(90)=109.51ms p(95)=136.46ms p(99.9)=190.52ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 269313
     http_req_receiving.............: avg=333.33µs min=24.23µs  med=54.85µs max=119.12ms p(90)=225.55µs p(95)=400.71µs p(99.9)=45.34ms 
     http_req_sending...............: avg=157.17µs min=4.24µs   med=9.48µs  max=149.63ms p(90)=18.66µs  p(95)=128.58µs p(99.9)=27.78ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=50.86ms  min=857.64µs med=42.84ms max=312.27ms p(90)=108.32ms p(95)=135.25ms p(99.9)=186.56ms
     http_reqs......................: 269313  4406.37202/s
     iteration_duration.............: avg=53.09ms  min=1.47ms   med=44ms    max=345.12ms p(90)=113.71ms p(95)=141.19ms p(99.9)=222.7ms 
     iterations.....................: 268313  4390.010492/s
     success_rate...................: 100.00% ✓ 268313      ✗ 0     
     vus............................: 62      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 801168      ✗ 0     
     data_received..................: 24 GB   384 MB/s
     data_sent......................: 322 MB  5.3 MB/s
     http_req_blocked...............: avg=58.67µs  min=1.02µs   med=2.56µs  max=135.23ms p(90)=4.18µs   p(95)=5.35µs   p(99.9)=19.98ms 
     http_req_connecting............: avg=53.95µs  min=0s       med=0s      max=117.09ms p(90)=0s       p(95)=0s       p(99.9)=19.35ms 
     http_req_duration..............: avg=51.8ms   min=835.7µs  med=43.12ms max=258.38ms p(90)=112.24ms p(95)=139.06ms p(99.9)=192.36ms
       { expected_response:true }...: avg=51.8ms   min=835.7µs  med=43.12ms max=258.38ms p(90)=112.24ms p(95)=139.06ms p(99.9)=192.36ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 268056
     http_req_receiving.............: avg=305.88µs min=25.61µs  med=51.79µs max=136.89ms p(90)=231.18µs p(95)=408.9µs  p(99.9)=41.55ms 
     http_req_sending...............: avg=139.08µs min=4.03µs   med=9.05µs  max=135.43ms p(90)=18.16µs  p(95)=133.16µs p(99.9)=25.45ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=51.36ms  min=796.33µs med=42.82ms max=258.31ms p(90)=111.13ms p(95)=137.92ms p(99.9)=188.16ms
     http_reqs......................: 268056  4391.259869/s
     iteration_duration.............: avg=53.34ms  min=1.39ms   med=44.03ms max=386.25ms p(90)=114.7ms  p(95)=142.84ms p(99.9)=216.02ms
     iterations.....................: 267056  4374.877994/s
     success_rate...................: 100.00% ✓ 267056      ✗ 0     
     vus............................: 59      min=0         max=497 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 779931      ✗ 0     
     data_received..................: 23 GB   373 MB/s
     data_sent......................: 314 MB  5.1 MB/s
     http_req_blocked...............: avg=45.12µs  min=862ns    med=2.23µs  max=113.96ms p(90)=3.91µs   p(95)=5.08µs   p(99.9)=14.21ms 
     http_req_connecting............: avg=41.92µs  min=0s       med=0s      max=113.75ms p(90)=0s       p(95)=0s       p(99.9)=13.87ms 
     http_req_duration..............: avg=53.43ms  min=990.46µs med=44.99ms max=290.44ms p(90)=113.6ms  p(95)=140.71ms p(99.9)=197.54ms
       { expected_response:true }...: avg=53.43ms  min=990.46µs med=44.99ms max=290.44ms p(90)=113.6ms  p(95)=140.71ms p(99.9)=197.54ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 260977
     http_req_receiving.............: avg=261.31µs min=24µs     med=50.87µs max=101.03ms p(90)=225.29µs p(95)=386.5µs  p(99.9)=33.09ms 
     http_req_sending...............: avg=121.52µs min=3.98µs   med=8.75µs  max=260.07ms p(90)=17.87µs  p(95)=127.73µs p(99.9)=20.96ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.05ms  min=947.49µs med=44.73ms max=289.99ms p(90)=112.81ms p(95)=139.76ms p(99.9)=194.23ms
     http_reqs......................: 260977  4264.25891/s
     iteration_duration.............: avg=54.79ms  min=1.63ms   med=46.01ms max=339.27ms p(90)=116.28ms p(95)=143.33ms p(99.9)=225.6ms 
     iterations.....................: 259977  4247.919313/s
     success_rate...................: 100.00% ✓ 259977      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 770703      ✗ 0     
     data_received..................: 23 GB   369 MB/s
     data_sent......................: 310 MB  5.1 MB/s
     http_req_blocked...............: avg=55.33µs  min=992ns    med=2.69µs  max=111.19ms p(90)=4.4µs    p(95)=5.6µs    p(99.9)=19.13ms 
     http_req_connecting............: avg=51.39µs  min=0s       med=0s      max=110.91ms p(90)=0s       p(95)=0s       p(99.9)=18.81ms 
     http_req_duration..............: avg=54.12ms  min=983.09µs med=45.3ms  max=304.3ms  p(90)=116.23ms p(95)=143.35ms p(99.9)=201.32ms
       { expected_response:true }...: avg=54.12ms  min=983.09µs med=45.3ms  max=304.3ms  p(90)=116.23ms p(95)=143.35ms p(99.9)=201.32ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 257901
     http_req_receiving.............: avg=289.19µs min=26.3µs   med=53.1µs  max=87.38ms  p(90)=240.21µs p(95)=415.16µs p(99.9)=38.3ms  
     http_req_sending...............: avg=133.82µs min=4.37µs   med=9.5µs   max=138.28ms p(90)=19.75µs  p(95)=136.88µs p(99.9)=23.57ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=53.7ms   min=931.42µs med=45.01ms max=303.82ms p(90)=115.32ms p(95)=142.24ms p(99.9)=197.13ms
     http_reqs......................: 257901  4213.793092/s
     iteration_duration.............: avg=55.45ms  min=1.66ms   med=46.19ms max=330.68ms p(90)=118.86ms p(95)=146.57ms p(99.9)=218.27ms
     iterations.....................: 256901  4197.454291/s
     success_rate...................: 100.00% ✓ 256901      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 762546      ✗ 0     
     data_received..................: 22 GB   366 MB/s
     data_sent......................: 307 MB  5.0 MB/s
     http_req_blocked...............: avg=46.17µs  min=741ns    med=2.14µs  max=117.11ms p(90)=3.88µs   p(95)=5.06µs   p(99.9)=11.82ms 
     http_req_connecting............: avg=43.05µs  min=0s       med=0s      max=116.97ms p(90)=0s       p(95)=0s       p(99.9)=11.08ms 
     http_req_duration..............: avg=54.81ms  min=716.48µs med=45.57ms max=313.74ms p(90)=116.19ms p(95)=144.11ms p(99.9)=212.24ms
       { expected_response:true }...: avg=54.81ms  min=716.48µs med=45.57ms max=313.74ms p(90)=116.19ms p(95)=144.11ms p(99.9)=212.24ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 255182
     http_req_receiving.............: avg=257.08µs min=24.72µs  med=51.3µs  max=213.79ms p(90)=216.63µs p(95)=377.02µs p(99.9)=35.69ms 
     http_req_sending...............: avg=121.61µs min=4.37µs   med=8.96µs  max=118.13ms p(90)=19.34µs  p(95)=127.32µs p(99.9)=22.14ms 
     http_req_tls_handshaking.......: avg=0s       min=0s       med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=54.43ms  min=659.57µs med=45.29ms max=297.24ms p(90)=115.4ms  p(95)=143.11ms p(99.9)=209.93ms
     http_reqs......................: 255182  4187.137534/s
     iteration_duration.............: avg=56.05ms  min=1.39ms   med=46.33ms max=338.6ms  p(90)=118.78ms p(95)=147.17ms p(99.9)=229.56ms
     iterations.....................: 254182  4170.729098/s
     success_rate...................: 100.00% ✓ 254182      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 500493      ✗ 0     
     data_received..................: 15 GB   239 MB/s
     data_sent......................: 202 MB  3.3 MB/s
     http_req_blocked...............: avg=16.19µs  min=822ns  med=2.39µs  max=44.05ms  p(90)=4.16µs   p(95)=5.45µs   p(99.9)=655.36µs
     http_req_connecting............: avg=12.96µs  min=0s     med=0s      max=43.92ms  p(90)=0s       p(95)=0s       p(99.9)=597.18µs
     http_req_duration..............: avg=84.71ms  min=1.22ms med=78.35ms max=348.7ms  p(90)=167.19ms p(95)=182.17ms p(99.9)=231.61ms
       { expected_response:true }...: avg=84.71ms  min=1.22ms med=78.35ms max=348.7ms  p(90)=167.19ms p(95)=182.17ms p(99.9)=231.61ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 167831
     http_req_receiving.............: avg=137.76µs min=25.7µs med=55.65µs max=38.36ms  p(90)=178.92µs p(95)=359.29µs p(99.9)=12.6ms  
     http_req_sending...............: avg=73.48µs  min=4.71µs med=10.45µs max=197.31ms p(90)=21.69µs  p(95)=127.43µs p(99.9)=9.4ms   
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=84.49ms  min=1.17ms med=78.15ms max=342.74ms p(90)=166.86ms p(95)=181.89ms p(99.9)=230.96ms
     http_reqs......................: 167831  2730.943513/s
     iteration_duration.............: avg=85.46ms  min=3.64ms med=79.3ms  max=356.49ms p(90)=167.63ms p(95)=182.58ms p(99.9)=232.11ms
     iterations.....................: 166831  2714.671528/s
     success_rate...................: 100.00% ✓ 166831      ✗ 0     
     vus............................: 77      min=0         max=493 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 248229      ✗ 0    
     data_received..................: 7.3 GB  117 MB/s
     data_sent......................: 101 MB  1.6 MB/s
     http_req_blocked...............: avg=5.34µs   min=972ns  med=2.27µs   max=10.36ms  p(90)=3.93µs   p(95)=4.83µs   p(99.9)=389.17µs
     http_req_connecting............: avg=2.41µs   min=0s     med=0s       max=10.28ms  p(90)=0s       p(95)=0s       p(99.9)=281.1µs 
     http_req_duration..............: avg=170.32ms min=2.01ms med=168.74ms max=546.49ms p(90)=323.2ms  p(95)=347.42ms p(99.9)=452.76ms
       { expected_response:true }...: avg=170.32ms min=2.01ms med=168.74ms max=546.49ms p(90)=323.2ms  p(95)=347.42ms p(99.9)=452.76ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 83743
     http_req_receiving.............: avg=74.61µs  min=27.3µs med=60.56µs  max=43.8ms   p(90)=97.23µs  p(95)=112.28µs p(99.9)=1.36ms  
     http_req_sending...............: avg=29.64µs  min=4.89µs med=10.44µs  max=188.18ms p(90)=16.79µs  p(95)=20.4µs   p(99.9)=2.88ms  
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=170.21ms min=1.95ms med=168.6ms  max=546.4ms  p(90)=323.11ms p(95)=347.32ms p(99.9)=452.68ms
     http_reqs......................: 83743   1340.102315/s
     iteration_duration.............: avg=172.6ms  min=4.55ms med=171.45ms max=546.64ms p(90)=323.95ms p(95)=348.04ms p(99.9)=453.27ms
     iterations.....................: 82743   1324.099756/s
     success_rate...................: 100.00% ✓ 82743       ✗ 0    
     vus............................: 81      min=0         max=493
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 245745      ✗ 0    
     data_received..................: 7.2 GB  116 MB/s
     data_sent......................: 100 MB  1.6 MB/s
     http_req_blocked...............: avg=5.28µs   min=932ns   med=2.41µs   max=7.01ms   p(90)=4.26µs   p(95)=5.2µs    p(99.9)=368.49µs
     http_req_connecting............: avg=2.18µs   min=0s      med=0s       max=6.94ms   p(90)=0s       p(95)=0s       p(99.9)=315.61µs
     http_req_duration..............: avg=172.08ms min=2.17ms  med=142.73ms max=802.97ms p(90)=361.51ms p(95)=420.09ms p(99.9)=641.74ms
       { expected_response:true }...: avg=172.08ms min=2.17ms  med=142.73ms max=802.97ms p(90)=361.51ms p(95)=420.09ms p(99.9)=641.74ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 82915
     http_req_receiving.............: avg=72.12µs  min=27.21µs med=58.19µs  max=40.95ms  p(90)=93.77µs  p(95)=108.14µs p(99.9)=1.36ms  
     http_req_sending...............: avg=29.53µs  min=4.84µs  med=11.05µs  max=119.71ms p(90)=17.89µs  p(95)=21.29µs  p(99.9)=3.36ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=171.98ms min=2.12ms  med=142.62ms max=802.86ms p(90)=361.43ms p(95)=420ms    p(99.9)=641.68ms
     http_reqs......................: 82915   1325.121769/s
     iteration_duration.............: avg=174.42ms min=6.14ms  med=145.25ms max=803.18ms p(90)=362.87ms p(95)=421.28ms p(99.9)=642.38ms
     iterations.....................: 81915   1309.14008/s
     success_rate...................: 100.00% ✓ 81915       ✗ 0    
     vus............................: 83      min=0         max=496
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 92355      ✗ 0    
     data_received..................: 2.8 GB  43 MB/s
     data_sent......................: 38 MB   592 kB/s
     http_req_blocked...............: avg=14.71µs  min=1.03µs  med=2.47µs   max=17.73ms p(90)=4.12µs   p(95)=5.06µs   p(99.9)=3.2ms 
     http_req_connecting............: avg=10.89µs  min=0s      med=0s       max=17.67ms p(90)=0s       p(95)=0s       p(99.9)=3.12ms
     http_req_duration..............: avg=452.14ms min=3.67ms  med=421.11ms max=1.87s   p(90)=893.04ms p(95)=980.97ms p(99.9)=1.47s 
       { expected_response:true }...: avg=452.14ms min=3.67ms  med=421.11ms max=1.87s   p(90)=893.04ms p(95)=980.97ms p(99.9)=1.47s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 31785
     http_req_receiving.............: avg=83.32µs  min=28.83µs med=67.53µs  max=65.03ms p(90)=104.54µs p(95)=118.57µs p(99.9)=1.49ms
     http_req_sending...............: avg=30.45µs  min=4.9µs   med=12.27µs  max=93.34ms p(90)=19µs     p(95)=21.31µs  p(99.9)=2.78ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=452.03ms min=3.61ms  med=421.04ms max=1.87s   p(90)=892.9ms  p(95)=980.88ms p(99.9)=1.47s 
     http_reqs......................: 31785   492.767698/s
     iteration_duration.............: avg=467.01ms min=17.93ms med=438.21ms max=1.88s   p(90)=897.57ms p(95)=983.79ms p(99.9)=1.48s 
     iterations.....................: 30785   477.264546/s
     success_rate...................: 100.00% ✓ 30785      ✗ 0    
     vus............................: 81      min=0        max=498
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 47190      ✗ 0    
     data_received..................: 1.5 GB  22 MB/s
     data_sent......................: 20 MB   298 kB/s
     http_req_blocked...............: avg=14.57µs  min=1.24µs  med=3.24µs   max=11.77ms p(90)=4.98µs   p(95)=6.62µs   p(99.9)=2.14ms
     http_req_connecting............: avg=9.78µs   min=0s      med=0s       max=11.7ms  p(90)=0s       p(95)=0s       p(99.9)=2.12ms
     http_req_duration..............: avg=869.89ms min=5.67ms  med=776.83ms max=4.71s   p(90)=1.77s    p(95)=1.99s    p(99.9)=3.97s 
       { expected_response:true }...: avg=869.89ms min=5.67ms  med=776.83ms max=4.71s   p(90)=1.77s    p(95)=1.99s    p(99.9)=3.97s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16730
     http_req_receiving.............: avg=95.33µs  min=28.66µs med=87.35µs  max=6.13ms  p(90)=125.59µs p(95)=141.89µs p(99.9)=1.37ms
     http_req_sending...............: avg=41.07µs  min=5.41µs  med=16.86µs  max=86.68ms p(90)=21.91µs  p(95)=25.3µs   p(99.9)=3.67ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=869.76ms min=5.57ms  med=776.72ms max=4.71s   p(90)=1.77s    p(95)=1.99s    p(99.9)=3.97s 
     http_reqs......................: 16730   248.179489/s
     iteration_duration.............: avg=925.23ms min=30.02ms med=844.5ms  max=4.72s   p(90)=1.79s    p(95)=2s       p(99.9)=4.01s 
     iterations.....................: 15730   233.345091/s
     success_rate...................: 100.00% ✓ 15730      ✗ 0    
     vus............................: 77      min=0        max=500
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 46815      ✗ 0    
     data_received..................: 1.5 GB  21 MB/s
     data_sent......................: 20 MB   291 kB/s
     http_req_blocked...............: avg=13.63µs  min=1.17µs  med=3.09µs   max=11.97ms p(90)=4.8µs    p(95)=6.46µs   p(99.9)=2ms     
     http_req_connecting............: avg=8.95µs   min=0s      med=0s       max=11.9ms  p(90)=0s       p(95)=0s       p(99.9)=1.96ms  
     http_req_duration..............: avg=873.81ms min=7.48ms  med=790.96ms max=3.08s   p(90)=1.78s    p(95)=1.9s     p(99.9)=2.58s   
       { expected_response:true }...: avg=873.81ms min=7.48ms  med=790.96ms max=3.08s   p(90)=1.78s    p(95)=1.9s     p(99.9)=2.58s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 16605
     http_req_receiving.............: avg=94.69µs  min=33.97µs med=87.3µs   max=52.87ms p(90)=123.14µs p(95)=138.96µs p(99.9)=674.38µs
     http_req_sending...............: avg=35.44µs  min=5.27µs  med=16.01µs  max=91.45ms p(90)=21.25µs  p(95)=24.6µs   p(99.9)=4.01ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=873.68ms min=7.4ms   med=790.86ms max=3.08s   p(90)=1.78s    p(95)=1.9s     p(99.9)=2.58s   
     http_reqs......................: 16605   242.408353/s
     iteration_duration.............: avg=929.79ms min=23.35ms med=882.68ms max=3.09s   p(90)=1.8s     p(95)=1.91s    p(99.9)=2.59s   
     iterations.....................: 15605   227.809837/s
     success_rate...................: 100.00% ✓ 15605      ✗ 0    
     vus............................: 81      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

