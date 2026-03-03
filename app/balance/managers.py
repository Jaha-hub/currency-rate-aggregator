from app.auth.models import User
from app.balance.models import Balance
from app.balance.repositories import BalanceRepository
from app.balance.schemas import WalletCreate


class BalanceManager:
    def __init__(self, session):
        self.session = session
        self.repo = BalanceRepository(session)

    async def create_wallet(self, user: User,request: WalletCreate) -> Balance:
        await self.repo.get_wallet_by_user_id(user.id)



        wallet  = await self.repo.create_wallet(user.id, **request.model_dump())
        await self.session.commit()
        return wallet


    async def update_wallet_balance(
        self,
        wallet_id: int,
        user_id: int,
        amount: int,
    ) -> Balance:
        """
        Обновляет баланс кошелька пользователя.
        Amount может быть положительным (пополнение)
        или отрицательным (списание).
        """

        # Получаем кошелек
        wallet = await self.repo.get_wallet_by_user_id(user_id)

        if not wallet or wallet.id != wallet_id:
            raise ValueError("Кошелек не найден")

        # 🔒 Защита от отрицательного баланса
        if wallet.balance + amount < 0:
            raise ValueError("Недостаточно средств")

        # Обновляем баланс
        updated_wallet = await self.repo.update_wallet_balance(
            wallet_id=wallet_id,
            user_id=user_id,
            amount=amount,
        )

        return updated_wallet

    async def get_wallet_by_user_id(
            self,
            user_id: int,

    ):
        return await self.repo.get_wallet_by_user_id(user_id)