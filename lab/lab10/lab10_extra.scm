;; Scheme ;;


(define lst
  (list (cons 1 nil) 2 (cons 3 (cons 4 nil)) 5)
)

(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (remove item lst)
  (filter-lst (lambda (x) (not (= x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  (if(null? s)
    s
    (cons (car s)
      (no-repeats (filter-lst (lambda (x) (not (= x (car s)))) (cdr s)))))
)

(define (substitute s old new)
  (cond
    ((null? s) s)
    ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
    ((eq? old (car s)) (cons new (substitute (cdr s) old new)))
    (else (cons (car s) (substitute (cdr s) old new))))
)


(define (sub-all s olds news)
  (cond
    ((null? s) s)
    ((null? olds) s)
    (else (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))))
)
