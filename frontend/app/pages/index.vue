<script setup>
const { fields_general,  fields_ratings, fields_house, fields_district, main, globalCounter} = useGlobalData()

const district_list = {
    bgColor: "bg-green-100",
    list: fields_district,
}

const house_list = {
    bgColor: "bg-blue-100",
    list: fields_house
}

const flat_list = {
    bgColor: "bg-fuchsia-100",
    list: fields_general
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
    </div>
    <div class="flex flex-col p-10 gap-5">
        <BlocksHeaderText>
            <template #primaryText>Критерии оценки при покупке квартиры</template>
            <template #secondaryText>Учитывается все самое важное и необходимое для комфортного проживания</template>
        </BlocksHeaderText>
        <div class="grid grid-cols-3 justify-around gap-5">
            <BlocksFlatInfo :title="'Инфраструктура района'" :list="district_list"/>
            <BlocksFlatInfo :title="'Стостояние дома'" :list="house_list"/>
            <BlocksFlatInfo :title="'Состояние квартиры'" :list="flat_list"/>
        </div>
    </div>
</template>
