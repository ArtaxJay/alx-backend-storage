-- This creates an index: idx_name_first
-- on d table names and the first letter of name.
CREATE INDEX idx_name_first ON names(name(1))