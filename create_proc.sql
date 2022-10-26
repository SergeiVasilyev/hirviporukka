-- An example for procedure which adds a new group

-- Create a procedure with 2 arguments, in is default 
CREATE PROCEDURE public.add_jakoryhma(
	seurue integer,
	ryhman_nimi character VARYING)

-- Language standart SQL
LANGUAGE SQL
AS $$ -- Begin
INSERT INTO public.jakoryhma (seurue_id, ryhman_nimi) VALUES (seurue, ryhman_nimi);
$$; -- End