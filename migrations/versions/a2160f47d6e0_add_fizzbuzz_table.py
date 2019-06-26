"""Add fizzbuzz table

Revision ID: a2160f47d6e0
Revises: 
Create Date: 2019-06-24 17:33:48.419406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a2160f47d6e0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE fizzbuzz(
            id VARCHAR(40) PRIMARY KEY NOT NULL,
            int1 INT NOT NULL,
            int2 INT NOT NULL,
            upper_bound INT NOT NULL,
            str1 VARCHAR(40) NOT NULL,
            str2 VARCHAR(40) NOT NULL,
            hits INT NOT NULL DEFAULT 1,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE OR REPLACE FUNCTION update_fizzbuzz_timestamp()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
    
        CREATE TRIGGER update_fizzbuzz_timestamp
        BEFORE UPDATE ON fizzbuzz
        FOR EACH ROW EXECUTE PROCEDURE update_fizzbuzz_timestamp();
        """
    )


def downgrade():
    op.drop_table("fizzbuzz")
