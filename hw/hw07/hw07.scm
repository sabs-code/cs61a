(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)

(define (rle s)
  (define (helper s prev count)
    (cond
    ((null? s) (cons-stream (list prev count) nil))
    ((= (car s) prev) (helper (cdr-stream s) prev (+ count 1)))
    (else (cons-stream (list prev count) (helper s (car s) 0)))
    ))
  (if (null? s) nil (helper s (car s) 0))
)
