"""db init

Revision ID: 621408ebd894
Revises:
Create Date: 2020-12-24 00:06:57.747079

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '621408ebd894'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    qn_table = op.create_table('question',
                               sa.Column('id', sa.Integer(), nullable=False,
                                         autoincrement=True),
                               sa.Column('created_at',
                                         sa.DateTime(), nullable=False),
                               sa.Column('content', sa.Text(),
                                         nullable=False),
                               sa.Column('likes',
                                         sa.Integer(), nullable=False, server_default="0"),
                               sa.Column('dislikes', sa.Integer(),
                                         nullable=False, server_default="0"),
                               sa.PrimaryKeyConstraint('id'),
                               )

    answer_table = op.create_table('answer',
                                   sa.Column('id', sa.Integer(), nullable=False,
                                             autoincrement=True),
                                   sa.Column('qn_id', sa.Integer(),
                                             nullable=False),
                                   sa.Column('content', sa.Text(),
                                             nullable=False),
                                   sa.Column('likes',
                                             sa.Integer(), nullable=False, server_default="0"),
                                   sa.Column('dislikes', sa.Integer(),
                                             nullable=False, server_default="0"),
                                   sa.PrimaryKeyConstraint(
                                       'id'),
                                   sa.ForeignKeyConstraint(
                                       ['qn_id'], ['question.id'],
                                       onupdate="CASCADE",
                                       ondelete="CASCADE"
                                   ),
                                   )

    tag_table = op.create_table('tag',
                                sa.Column('id', sa.Integer(), nullable=False),
                                sa.Column('tag', sa.String(
                                    255), nullable=False),
                                sa.PrimaryKeyConstraint(
                                    'id', 'tag', name='tag_pk'),
                                sa.ForeignKeyConstraint(
                                    ['id'], ['question.id'],
                                    onupdate="CASCADE",
                                    ondelete="CASCADE"),
                                )


def downgrade():
    op.drop_table('question')
    op.drop_table('answer')
    op.drop_table('tag')
