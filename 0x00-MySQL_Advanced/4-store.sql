-- Creates trigger that decreases quantity of item after new order
-- Change delimiter
DELIMITER $$

-- Trigger to decrease quantity of item after adding new order
CREATE TRIGGER dec_quantity AFTER INSERT ON orders
   FOR EACH ROW
   BEGIN
	UPDATE items
           SET quantity = quantity - NEW.number
         WHERE name = NEW.item_name;
   END$$

-- Reset delimiter
DELIMITER ;
