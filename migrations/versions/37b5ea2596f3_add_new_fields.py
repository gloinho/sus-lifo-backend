"""add new fields

Revision ID: 37b5ea2596f3
Revises: 0e0bcf6ffec2
Create Date: 2023-12-21 14:04:06.790682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37b5ea2596f3'
down_revision = '0e0bcf6ffec2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('createdAt', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
        batch_op.add_column(sa.Column('updatedAt', sa.DateTime(timezone=True), nullable=True))
        batch_op.add_column(sa.Column('assisted', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.drop_column('assisted')
        batch_op.drop_column('updatedAt')
        batch_op.drop_column('createdAt')

    # ### end Alembic commands ###