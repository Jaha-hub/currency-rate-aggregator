from app.auth.models import User
from app.wallet.models import Wallet
from app.wallet.repositories import WalletRepository
from app.wallet.schemas import WalletCreate


class WalletManager:
    def __init__(self, session):
        self.session = session
        self.repo = WalletRepository(session)

    async def create_wallet(self, user: User, wallet: Wallet,request: WalletCreate) -> Wallet:
        existing_wallet = await self.repo.get_wallet_by_user_id(user.id, wallet)

        if existing_wallet:
            raise ValueError("У пользователя уже есть кошелек")

        wallet = Wallet(user_id=user.id, balance=0)

        return await self.repo.create_wallet(wallet, **request.model_dump())

    async def update_wallet_balance(
        self,
        wallet_id: int,
        user_id: int,
        amount: int,
    ) -> Wallet:
        """
        Обновляет баланс кошелька пользователя.
        amount может быть положительным (пополнение)
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
            wallet: Wallet,
    ):
        return await self.repo.get_wallet_by_user_id(user_id, wallet)