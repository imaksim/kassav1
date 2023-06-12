CREATE TABLE public.stuff
(
    id integer NOT NULL DEFAULT nextval('stuff_id_seq'::regclass),
    name character varying(32)[] COLLATE pg_catalog."default" NOT NULL,
    email character varying(32)[] COLLATE pg_catalog."default" NOT NULL,
    active boolean NOT NULL DEFAULT true,
    CONSTRAINT stuff_pkey PRIMARY KEY (id)
)