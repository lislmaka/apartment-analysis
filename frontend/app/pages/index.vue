<script setup>
const district_list = {
    bgColor: "bg-green-100",
    list: [
        { label: "Сетевые магазины (Пятерочка, Магнит и т.д.)", value: "< 500 м." },
        { label: "Пункты доставки (Ozon, WD)", value: "< 500 м." },
        { label: "Аптека", value: "< 500 м." },
        { label: "Отделение Банка", value: "< 500 м." },
        { label: "Отделение Почты", value: "< 500 м." },
    ],
}

const house_list = {
    bgColor: "bg-blue-100",
    list: [
        { label: "Дата капремонта", value: "< 5 лет" },
        { label: "Дата замены лифта", value: "Да?/Нет" },
        { label: "Ступеньки перед подьездом", value: "Да?/Нет" },
        { label: "Мусоропровод", value: "Да?/Нет" },
        { label: "Общий коридор", value: "Да?/Нет" },
    ],
}

const flat_list = {
    bgColor: "bg-fuchsia-100",
    list: [
        { label: "Состояние туалета", value: "Хорошо/Плохо" },
        { label: "Состояние ванной комнаты", value: "Хорошо/Плохо" },
        { label: "Состояние балкона", value: "Хорошо/Плохо" },
        { label: "Состояние кухни", value: "Хорошо/Плохо" },
        { label: "Соседи сверху", value: "Хорошо/Плохо" },
        { label: "Соседи снизу", value: "Хорошо/Плохо" },
    ],
}
</script>
<template>
    <div class="flex flex-col text-center rounded-md mt-5 p-10 space-y-10 bg-gray-100">
        <div class="text-7xl font-bold">
            Анализируем квартиры перед покупкой
        </div>
        <div class="text-3xl">
            На основании данных из открытых источников<br> по трем составным критериям
        </div>
        <!-- <div class="flex justify-center space-x-5">
            <BlockInfoBlockText>Стостояние квартиры</BlockInfoBlockText>
            <BlockInfoBlockText>Состояние дома</BlockInfoBlockText>
            <BlockInfoBlockText>Инфраструктура района</BlockInfoBlockText>
        </div> -->
    </div>
    <div class="flex flex-col p-10 gap-5">
        <BlockHeaderText>
            <template #primaryText>Критерии оценки при покупке квартиры</template>
            <template #secondaryText>Суммарно учитывается более 15 характеристик</template>
            <!-- <template v-slot="secondaryText">Критерии оценки</template> -->
        </BlockHeaderText>
        <div class="grid grid-cols-3 justify-around gap-5">
            <BlockInfoList :title="'Инфраструктура района'" :list="district_list"></BlockInfoList>
            <BlockInfoList :title="'Стостояние дома'" :list="house_list"></BlockInfoList>
            <BlockInfoList :title="'Состояние квартиры'" :list="flat_list"></BlockInfoList>
        </div>
    </div>
</template>

<!-- <template>
    <div class="flex justify-between border border-gray-300 rounded mt-5 p-5">
        <div class="flex flex-col space-y-7">
            <div class="text-7xl font-bold">
                Анализируем квартиры перед покупкой
            </div>
            <div class="text-3xl">
                На основании данных из открытых источников по трем составным критериям
            </div>
            <div class="text-3xl">
                
            </div>
        </div>

        <div class="w-sm">
            <img class="shrink-0 rounded-2xl shadow-2xl" :src="'/public/frontend/main.jpg'" alt="">
        </div>
    </div>
</template> -->
