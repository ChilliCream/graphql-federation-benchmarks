## Overview for: `burst-vus`

Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs ([HotChocolate](https://github.com/ChilliCream/graphql-platform)) and executes a heavy nested query that exercises federation/composition capabilities.

**Methodology:** Each gateway executes 10 runs of 120s each. The first run is a full-duration warmup (discarded). The remaining 9 runs are measured. Results are ranked by **median RPS** across the 9 measured runs, with best/worst/CV% reported for transparency.

This scenario is a burst stress test with peaks up to **500 VUs** over **120s**.


### HotChocolate Subgraphs

| Gateway | Version | Median RPS | Best RPS | Worst RPS | CV% | Notes |
| :------ | :------ | ---------: | -------: | --------: | --: | :---- |
| fusion-nightly-net-11 | 16.7.0-p.27 | 2,500 | 2,592 | 2,492 | 1.4% |  |
| fusion-net-10 | 16.6.8 | 2,432 | 2,538 | 2,383 | 2.1% |  |
| fusion-nightly-net-10 | 16.7.0-p.27 | 2,360 | 2,471 | 2,351 | 1.8% |  |
| hive-router | v0.3.5 | 2,302 | 2,463 | 2,277 | 2.7% |  |
| fusion-nightly-fed-net-10 | 16.7.0-p.27 | 2,185 | 2,286 | 2,173 | 1.9% |  |
| cosmo | 0.359.0 | 1,284 | 1,339 | 1,278 | 1.6% |  |
| caliban | 3.2.0 | 1,267 | 1,333 | 1,259 | 2.1% |  |
| hive-gateway-router-runtime | 2.15.2 | 471 | 481 | 468 | 0.9% |  |
| apollo-gateway | 2.14.4 | 236 | 241 | 235 | 0.7% |  |
| hive-gateway | 2.15.2 | 232 | 237 | 230 | 1.1% |  |
| apollo-router | v2.18.0 | — | — | — | — | non-compatible response (39068 across 9/9 runs) |
| apollo-router-v3 | v3.0.0-preview.0 | — | — | — | — | non-compatible response (10324 across 9/9 runs) |
| feddi-gateway | — | — | — | — | — | not run |
| grafbase | 0.53.5 | — | — | — | — | non-compatible response (322790 across 9/9 runs) |


### Details

<details>
  <summary>Summary for: fusion-nightly-net-11 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 459942      ✗ 0     
     data_received..................: 14 GB   219 MB/s
     data_sent......................: 185 MB  3.0 MB/s
     http_req_blocked...............: avg=18.12µs min=862ns   med=2.26µs   max=49.42ms  p(90)=4µs      p(95)=5.21µs   p(99.9)=1.94ms  
     http_req_connecting............: avg=14.95µs min=0s      med=0s       max=48.23ms  p(90)=0s       p(95)=0s       p(99.9)=1.82ms  
     http_req_duration..............: avg=92.13ms min=1.38ms  med=86.83ms  max=491.97ms p(90)=176.39ms p(95)=194.45ms p(99.9)=298.2ms 
       { expected_response:true }...: avg=92.13ms min=1.38ms  med=86.83ms  max=491.97ms p(90)=176.39ms p(95)=194.45ms p(99.9)=298.2ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 154314
     http_req_receiving.............: avg=1.45ms  min=54.29µs med=130.76µs max=271.75ms p(90)=3.33ms   p(95)=5.54ms   p(99.9)=45.64ms 
     http_req_sending...............: avg=71.46µs min=4.58µs  med=9.37µs   max=182.93ms p(90)=21.47µs  p(95)=117.58µs p(99.9)=8.95ms  
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=90.6ms  min=1.31ms  med=85.37ms  max=436.05ms p(90)=174.67ms p(95)=192.47ms p(99.9)=281.8ms 
     http_reqs......................: 154314  2500.369389/s
     iteration_duration.............: avg=92.99ms min=3.16ms  med=87.8ms   max=492.16ms p(90)=176.85ms p(95)=194.9ms  p(99.9)=300.09ms
     iterations.....................: 153314  2484.166261/s
     success_rate...................: 100.00% ✓ 153314      ✗ 0     
     vus............................: 89      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-net-10 (HotChocolate subgraphs) (16.6.8)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 448842      ✗ 0     
     data_received..................: 13 GB   213 MB/s
     data_sent......................: 181 MB  2.9 MB/s
     http_req_blocked...............: avg=18.42µs min=861ns  med=2.25µs  max=99.33ms  p(90)=4.04µs   p(95)=5.24µs   p(99.9)=2.22ms  
     http_req_connecting............: avg=15.38µs min=0s     med=0s      max=99.26ms  p(90)=0s       p(95)=0s       p(99.9)=2.15ms  
     http_req_duration..............: avg=94.45ms min=1.55ms med=81.41ms max=1.31s    p(90)=181.47ms p(95)=210.58ms p(99.9)=732.3ms 
       { expected_response:true }...: avg=94.45ms min=1.55ms med=81.41ms max=1.31s    p(90)=181.47ms p(95)=210.58ms p(99.9)=732.3ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 150614
     http_req_receiving.............: avg=1.35ms  min=49.6µs med=99.83µs max=643.83ms p(90)=1.58ms   p(95)=4.29ms   p(99.9)=72.14ms 
     http_req_sending...............: avg=70.75µs min=4.72µs med=9.48µs  max=142.77ms p(90)=20.35µs  p(95)=113.59µs p(99.9)=9.47ms  
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=93.02ms min=1.44ms med=80.32ms max=1.31s    p(90)=179.98ms p(95)=207.97ms p(99.9)=724.43ms
     http_reqs......................: 150614  2432.733506/s
     iteration_duration.............: avg=95.37ms min=2.75ms med=82.28ms max=1.31s    p(90)=182.1ms  p(95)=211.37ms p(99.9)=733.84ms
     iterations.....................: 149614  2416.581399/s
     success_rate...................: 100.00% ✓ 149614      ✗ 0     
     vus............................: 54      min=0         max=499 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-net-10 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 435087      ✗ 0     
     data_received..................: 13 GB   207 MB/s
     data_sent......................: 175 MB  2.8 MB/s
     http_req_blocked...............: avg=17.21µs min=831ns   med=2.33µs   max=55.65ms  p(90)=4.13µs   p(95)=5.26µs   p(99.9)=1.96ms  
     http_req_connecting............: avg=14.02µs min=0s      med=0s       max=55.46ms  p(90)=0s       p(95)=0s       p(99.9)=1.9ms   
     http_req_duration..............: avg=97.43ms min=1.46ms  med=83.41ms  max=1.82s    p(90)=180.46ms p(95)=210.72ms p(99.9)=758.4ms 
       { expected_response:true }...: avg=97.43ms min=1.46ms  med=83.41ms  max=1.82s    p(90)=180.46ms p(95)=210.72ms p(99.9)=758.4ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 146029
     http_req_receiving.............: avg=1.78ms  min=52.39µs med=107.08µs max=1.22s    p(90)=1.96ms   p(95)=5.36ms   p(99.9)=129.28ms
     http_req_sending...............: avg=66.72µs min=4.69µs  med=9.24µs   max=237.52ms p(90)=18.94µs  p(95)=111.8µs  p(99.9)=8.6ms   
     http_req_tls_handshaking.......: avg=0s      min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=95.59ms min=1.38ms  med=81.97ms  max=1.82s    p(90)=178.16ms p(95)=206.64ms p(99.9)=729.67ms
     http_reqs......................: 146029  2360.313963/s
     iteration_duration.............: avg=98.37ms min=2.57ms  med=84.36ms  max=1.82s    p(90)=181ms    p(95)=211.43ms p(99.9)=759.01ms
     iterations.....................: 145029  2344.150639/s
     success_rate...................: 100.00% ✓ 145029      ✗ 0     
     vus............................: 51      min=0         max=499 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 425409      ✗ 0     
     data_received..................: 13 GB   201 MB/s
     data_sent......................: 172 MB  2.8 MB/s
     http_req_blocked...............: avg=14.94µs  min=932ns   med=2.33µs  max=45.3ms   p(90)=3.98µs   p(95)=5.26µs   p(99.9)=1.33ms  
     http_req_connecting............: avg=11.84µs  min=0s      med=0s      max=45.23ms  p(90)=0s       p(95)=0s       p(99.9)=1.24ms  
     http_req_duration..............: avg=99.6ms   min=1.6ms   med=94.82ms max=288.06ms p(90)=192.44ms p(95)=207.92ms p(99.9)=251.96ms
       { expected_response:true }...: avg=99.6ms   min=1.6ms   med=94.82ms max=288.06ms p(90)=192.44ms p(95)=207.92ms p(99.9)=251.96ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 142803
     http_req_receiving.............: avg=118.35µs min=28.49µs med=56.53µs max=79.01ms  p(90)=126.11µs p(95)=336.92µs p(99.9)=8.38ms  
     http_req_sending...............: avg=56.38µs  min=4.99µs  med=10.24µs max=155.12ms p(90)=19.42µs  p(95)=116.84µs p(99.9)=7.37ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=99.43ms  min=1.55ms  med=94.64ms max=287.99ms p(90)=192.2ms  p(95)=207.66ms p(99.9)=251.11ms
     http_reqs......................: 142803  2302.87204/s
     iteration_duration.............: avg=100.55ms min=3.66ms  med=95.97ms max=321.13ms p(90)=192.93ms p(95)=208.34ms p(99.9)=253.03ms
     iterations.....................: 141803  2286.745824/s
     success_rate...................: 100.00% ✓ 141803      ✗ 0     
     vus............................: 57      min=0         max=498 
     vus_max........................: 500     min=500       max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

<details>
  <summary>Summary for: fusion-nightly-fed-net-10 (HotChocolate subgraphs) (16.7.0-p.27)</summary>

  **K6 Output**


```
✓ response code was 200
     ✓ no graphql errors
     ✓ valid response structure

     checks.........................: 100.00% ✓ 404931      ✗ 0     
     data_received..................: 12 GB   192 MB/s
     data_sent......................: 163 MB  2.6 MB/s
     http_req_blocked...............: avg=14.14µs  min=872ns   med=2.3µs   max=56.58ms  p(90)=4.04µs   p(95)=5.19µs   p(99.9)=1.62ms  
     http_req_connecting............: avg=10.96µs  min=0s      med=0s      max=56.5ms   p(90)=0s       p(95)=0s       p(99.9)=1.48ms  
     http_req_duration..............: avg=104.66ms min=1.77ms  med=92.92ms max=1.25s    p(90)=196.52ms p(95)=226.91ms p(99.9)=796.98ms
       { expected_response:true }...: avg=104.66ms min=1.77ms  med=92.92ms max=1.25s    p(90)=196.52ms p(95)=226.91ms p(99.9)=796.98ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 135977
     http_req_receiving.............: avg=1.34ms   min=50.67µs med=109.3µs max=798.47ms p(90)=1.68ms   p(95)=4.06ms   p(99.9)=92.62ms 
     http_req_sending...............: avg=63.37µs  min=4.83µs  med=9.83µs  max=44.77ms  p(90)=20.23µs  p(95)=111.05µs p(99.9)=8.55ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=103.25ms min=1.64ms  med=91.92ms max=1.25s    p(90)=194.92ms p(95)=224.3ms  p(99.9)=770.75ms
     http_reqs......................: 135977  2185.940277/s
     iteration_duration.............: avg=105.69ms min=3.71ms  med=94.07ms max=1.25s    p(90)=197.05ms p(95)=227.62ms p(99.9)=797.28ms
     iterations.....................: 134977  2169.864468/s
     success_rate...................: 100.00% ✓ 134977      ✗ 0     
     vus............................: 66      min=0         max=496 
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 239496      ✗ 0    
     data_received..................: 7.1 GB  112 MB/s
     data_sent......................: 97 MB   1.5 MB/s
     http_req_blocked...............: avg=6.72µs   min=1.07µs  med=2.94µs   max=26.51ms  p(90)=4.93µs   p(95)=5.98µs   p(99.9)=532.15µs
     http_req_connecting............: avg=3.08µs   min=0s      med=0s       max=26.32ms  p(90)=0s       p(95)=0s       p(99.9)=436.6µs 
     http_req_duration..............: avg=176.43ms min=2.21ms  med=174.55ms max=463.39ms p(90)=333.85ms p(95)=358.29ms p(99.9)=425.7ms 
       { expected_response:true }...: avg=176.43ms min=2.21ms  med=174.55ms max=463.39ms p(90)=333.85ms p(95)=358.29ms p(99.9)=425.7ms 
     http_req_failed................: 0.00%   ✓ 0           ✗ 80832
     http_req_receiving.............: avg=85.36µs  min=27.01µs med=67.62µs  max=37.47ms  p(90)=109.75µs p(95)=127.81µs p(99.9)=1.7ms   
     http_req_sending...............: avg=34.46µs  min=5.26µs  med=13.24µs  max=130.3ms  p(90)=20.87µs  p(95)=25.11µs  p(99.9)=3.92ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=176.31ms min=2.12ms  med=174.44ms max=463.32ms p(90)=333.72ms p(95)=358.17ms p(99.9)=425.43ms
     http_reqs......................: 80832   1284.962906/s
     iteration_duration.............: avg=178.9ms  min=4.94ms  med=177.53ms max=482.04ms p(90)=334.7ms  p(95)=358.87ms p(99.9)=426.21ms
     iterations.....................: 79832   1269.066196/s
     success_rate...................: 100.00% ✓ 79832       ✗ 0    
     vus............................: 53      min=0         max=499
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

     checks.........................: 100.00% ✓ 236469      ✗ 0    
     data_received..................: 7.0 GB  111 MB/s
     data_sent......................: 96 MB   1.5 MB/s
     http_req_blocked...............: avg=8.49µs   min=1.17µs  med=3.4µs    max=30.46ms  p(90)=5.37µs   p(95)=6.47µs   p(99.9)=647.5µs 
     http_req_connecting............: avg=4.33µs   min=0s      med=0s       max=30.41ms  p(90)=0s       p(95)=0s       p(99.9)=567.42µs
     http_req_duration..............: avg=178.76ms min=2.39ms  med=153.35ms max=989.77ms p(90)=366.29ms p(95)=433.91ms p(99.9)=712.11ms
       { expected_response:true }...: avg=178.76ms min=2.39ms  med=153.35ms max=989.77ms p(90)=366.29ms p(95)=433.91ms p(99.9)=712.11ms
     http_req_failed................: 0.00%   ✓ 0           ✗ 79823
     http_req_receiving.............: avg=91.67µs  min=31.73µs med=69.18µs  max=132.21ms p(90)=109.83µs p(95)=129.58µs p(99.9)=2.38ms  
     http_req_sending...............: avg=43.37µs  min=5.31µs  med=14.02µs  max=160.47ms p(90)=21.06µs  p(95)=25.56µs  p(99.9)=4.67ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=178.62ms min=2.32ms  med=153.23ms max=989.71ms p(90)=366.18ms p(95)=433.81ms p(99.9)=712.01ms
     http_reqs......................: 79823   1267.318393/s
     iteration_duration.............: avg=181.3ms  min=7.33ms  med=156.08ms max=990.01ms p(90)=368.08ms p(95)=435.22ms p(99.9)=714.4ms 
     iterations.....................: 78823   1251.441786/s
     success_rate...................: 100.00% ✓ 78823       ✗ 0    
     vus............................: 56      min=0         max=498
     vus_max........................: 500     min=500       max=500
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

     checks.........................: 100.00% ✓ 89004      ✗ 0    
     data_received..................: 2.7 GB  41 MB/s
     data_sent......................: 37 MB   565 kB/s
     http_req_blocked...............: avg=7.87µs   min=951ns   med=3.05µs   max=11.07ms  p(90)=4.76µs   p(95)=5.75µs   p(99.9)=692.74µs
     http_req_connecting............: avg=3.81µs   min=0s      med=0s       max=10.99ms  p(90)=0s       p(95)=0s       p(99.9)=665.84µs
     http_req_duration..............: avg=468.48ms min=4.04ms  med=437.78ms max=1.87s    p(90)=932.17ms p(95)=1s       p(99.9)=1.49s   
       { expected_response:true }...: avg=468.48ms min=4.04ms  med=437.78ms max=1.87s    p(90)=932.17ms p(95)=1s       p(99.9)=1.49s   
     http_req_failed................: 0.00%   ✓ 0          ✗ 30668
     http_req_receiving.............: avg=95.43µs  min=29.12µs med=76.9µs   max=149.12ms p(90)=114.91µs p(95)=130.18µs p(99.9)=942.29µs
     http_req_sending...............: avg=29.85µs  min=4.89µs  med=14.8µs   max=91.69ms  p(90)=21.12µs  p(95)=23.83µs  p(99.9)=2.09ms  
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s       p(90)=0s       p(95)=0s       p(99.9)=0s      
     http_req_waiting...............: avg=468.36ms min=3.97ms  med=437.62ms max=1.87s    p(90)=932.08ms p(95)=1s       p(99.9)=1.49s   
     http_reqs......................: 30668   471.039006/s
     iteration_duration.............: avg=484.5ms  min=28.89ms med=457.15ms max=1.87s    p(90)=936.8ms  p(95)=1.01s    p(99.9)=1.5s    
     iterations.....................: 29668   455.679706/s
     success_rate...................: 100.00% ✓ 29668      ✗ 0    
     vus............................: 60      min=0        max=498
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

     checks.........................: 100.00% ✓ 45930      ✗ 0    
     data_received..................: 1.4 GB  21 MB/s
     data_sent......................: 20 MB   284 kB/s
     http_req_blocked...............: avg=19.43µs  min=1.34µs  med=3.77µs   max=8.77ms  p(90)=5.74µs  p(95)=7.57µs   p(99.9)=4.39ms
     http_req_connecting............: avg=13.03µs  min=0s      med=0s       max=6ms     p(90)=0s      p(95)=0s       p(99.9)=4.16ms
     http_req_duration..............: avg=890.58ms min=7.89ms  med=802.49ms max=3.03s   p(90)=1.81s   p(95)=1.92s    p(99.9)=2.78s 
       { expected_response:true }...: avg=890.58ms min=7.89ms  med=802.49ms max=3.03s   p(90)=1.81s   p(95)=1.92s    p(99.9)=2.78s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 16310
     http_req_receiving.............: avg=103.76µs min=37.36µs med=93.88µs  max=49.52ms p(90)=133.9µs p(95)=151.77µs p(99.9)=1.15ms
     http_req_sending...............: avg=33.43µs  min=6.19µs  med=17.96µs  max=26.41ms p(90)=23.94µs p(95)=27.64µs  p(99.9)=3.49ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=890.45ms min=7.75ms  med=802.37ms max=3.03s   p(90)=1.81s   p(95)=1.92s    p(99.9)=2.78s 
     http_reqs......................: 16310   236.89956/s
     iteration_duration.............: avg=948.71ms min=46.64ms med=868.75ms max=3.04s   p(90)=1.82s   p(95)=1.93s    p(99.9)=2.8s  
     iterations.....................: 15310   222.374756/s
     success_rate...................: 100.00% ✓ 15310      ✗ 0    
     vus............................: 96      min=0        max=500
     vus_max........................: 500     min=500      max=500
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

     checks.........................: 100.00% ✓ 44463      ✗ 0    
     data_received..................: 1.4 GB  20 MB/s
     data_sent......................: 19 MB   279 kB/s
     http_req_blocked...............: avg=15.09µs  min=1.18µs  med=3.23µs   max=6.25ms  p(90)=5.01µs  p(95)=6.65µs   p(99.9)=2.33ms
     http_req_connecting............: avg=10.2µs   min=0s      med=0s       max=6.04ms  p(90)=0s      p(95)=0s       p(99.9)=2.31ms
     http_req_duration..............: avg=922.52ms min=6.14ms  med=838.72ms max=5.47s   p(90)=1.86s   p(95)=2.07s    p(99.9)=4.64s 
       { expected_response:true }...: avg=922.52ms min=6.14ms  med=838.72ms max=5.47s   p(90)=1.86s   p(95)=2.07s    p(99.9)=4.64s 
     http_req_failed................: 0.00%   ✓ 0          ✗ 15821
     http_req_receiving.............: avg=97.21µs  min=33.71µs med=90.19µs  max=5.7ms   p(90)=129.2µs p(95)=144.71µs p(99.9)=1.17ms
     http_req_sending...............: avg=35.98µs  min=5.74µs  med=16.22µs  max=77.25ms p(90)=21.43µs p(95)=24.83µs  p(99.9)=3.04ms
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s       max=0s      p(90)=0s      p(95)=0s       p(99.9)=0s    
     http_req_waiting...............: avg=922.39ms min=6.06ms  med=838.58ms max=5.47s   p(90)=1.86s   p(95)=2.07s    p(99.9)=4.64s 
     http_reqs......................: 15821   232.687839/s
     iteration_duration.............: avg=984.8ms  min=37.07ms med=907.32ms max=5.47s   p(90)=1.89s   p(95)=2.08s    p(99.9)=4.67s 
     iterations.....................: 14821   217.980309/s
     success_rate...................: 100.00% ✓ 14821      ✗ 0    
     vus............................: 48      min=0        max=500
     vus_max........................: 500     min=500      max=500
```


  **Performance Overview**


  **no-image-available**



  **HTTP Overview**


  **no-image-available**


</details>

### Footnotes

- Benchmark hardware #1: host=bench-001, os=Linux 6.8.0-147-generic, cpu=AMD Ryzen 7 5700G with Radeon Graphics, cores=16 logical (16 CPUs), ram=122 GB

