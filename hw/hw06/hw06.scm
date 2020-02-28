;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (unique s)
    (if (null? s) 
        s 
        (cons (car s)
            (unique (filter (lambda (x) (not (eq? (car s) x))) (cdr s)))))
)

(define (cons-all first rests)
  (map (lambda (x) (cons first x)) rests)
)

;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
         (cond
            ((= total 0) (list()))
            ((< total 0) nil)
            ((null? denoms) nil)
            (else (append
                 (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) 
                 (list-change total (cdr denoms))))
      )
  )

; Tail recursion

(define (replicate x n)
  (define (helper x n r)
      (if (= n 0) r
        (helper x (- n 1) (cons x r))))
  (helper x n nil)
  )

(define (accumulate combiner start n term)
  (if (= n 0) start
  (combiner (term n) (accumulate combiner start (- n 1) term)))
)

(define (accumulate-tail combiner start n term)
  (define (helper n result)
      (if (= n 0) result 
          (helper (- n 1) (combiner result (term n)))))
    (helper n start)
)


; Macros

(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)