CREATE TABLE public.authors (
	id bigserial NOT NULL,
	first_name varchar NULL,
	last_name varchar NULL,
	CONSTRAINT authors_pk PRIMARY KEY (id)
);

CREATE TABLE public.books (
	id bigserial NOT NULL,
	title varchar NULL,
	num_pages int4 NULL,
	CONSTRAINT books_pk PRIMARY KEY (id)
);

CREATE TABLE public.authorbooks (
	id bigserial NOT NULL,
	author_id int8 NOT NULL,
	book_id int8 NOT NULL,
	CONSTRAINT authorbooks_pk PRIMARY KEY (id),
	CONSTRAINT authorbooks_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.authors(id),
	CONSTRAINT authorbooks_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(id)
);