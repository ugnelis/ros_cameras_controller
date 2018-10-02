CREATE TABLE IF NOT EXISTS cameras
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    name character(80),
    url character(2083),
    created_at timestamp(0) without time zone NOT NULL DEFAULT now(),
    CONSTRAINT cameras_pkey PRIMARY KEY (id)
);
